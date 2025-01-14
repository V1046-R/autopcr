import quart
from quart import request, render_template, Blueprint
import os
import json
from typing import Callable, Coroutine, Any
from ..module.accountmgr import Account, instance as accountmgr, AccountException
from ..constants import CONFIG_PATH

class HttpServer:
    def __init__(self, host = '0.0.0.0', port = 2, qq_only = False):
        self.app = Blueprint('autopcr', __name__, static_folder='assets', static_url_path='/assets', url_prefix="/daily")
        self.quart = quart.Quart(__name__)
        self.host = host
        self.port = port
        self.configure_routes()
        self.qq_only = qq_only
    
    @staticmethod
    def wrapaccount(readonly: bool = False):
        def wrapper(func: Callable[[Account], Coroutine[Any, Any, Any]]):
            async def inner():
                acc = request.args.get('account')
                if acc is None:
                    return 'No account specified', 400
                try:
                    async with accountmgr.load(acc, readonly) as mgr:
                        return await func(mgr)
                except AccountException as e:
                    return str(e), 400
            inner.__name__ = func.__name__
            return inner
        return wrapper

    def configure_routes(self):
        # backend
        @self.app.route('/api/config', methods = ['GET'])
        @HttpServer.wrapaccount(readonly = True)
        async def get_config(mgr: Account):
            return mgr.generate_daily_info()

        @self.app.route('/api/info', methods = ['GET'])
        @HttpServer.wrapaccount(readonly = True)
        async def get_info(mgr: Account):
            return mgr.generate_info()

        @self.app.route('/api/info', methods = ['PUT'])
        @HttpServer.wrapaccount()
        async def update_info(mgr: Account):
            data = await request.get_json()
            if not(data['username'] or mgr.data['username'] ) or not (data['password'] or mgr.data['password']):
                return 'Incomplete Account!', 400
            elif self.qq_only and not (data['qq'] or mgr.qq):
                return "Need QQ!", 400
            else:
                for key in ['alian', 'username', 'password', 'qq']:
                    if data[key] and len(data[key]) <= 64:
                        mgr.data[key] = data[key]
                return "ok", 200

        @self.app.route('/api/config', methods = ['PUT'])
        @HttpServer.wrapaccount()
        async def update_config(mgr: Account):
            data = await request.get_json()

            mgr.data['config'] = data

            return "ok", 200

        @self.app.route('/api/tools', methods = ['PUT'])
        @HttpServer.wrapaccount()
        async def update_tools(mgr: Account):
            # save TODO

            return "ok", 200

        @self.app.route('/api/config', methods = ['DELETE'])
        async def delete_config():

            file = request.args.get('account')
            if file is None or not accountmgr.pathsyntax.fullmatch(file):
                return 'Invalid account', 400

            accountmgr.delete(file)

            return "ok", 200

        @self.app.route('/api/config', methods = ['POST'])
        async def new_config():
            # if self.qq_only:
            #     return 'Please contact the maintenance to register', 400
            file = request.args.get('account')
            if file is None or not accountmgr.pathsyntax.fullmatch(file):
                return 'Invalid account', 400
                
            fn = os.path.join(CONFIG_PATH, file) + '.json'

            if os.path.exists(fn):
                return 'Account already exists', 400

            data = await request.get_json()
            with open(fn, 'w') as f:
                f.write(json.dumps(data))
            return '', 204

        @self.app.route('/api/login', methods = ['GET'])
        async def login_account_check():
            # if self.qq_only:
            #     return 'Please contact the maintenance to register', 400
            file = request.args.get('account')
            if file is None or not accountmgr.pathsyntax.fullmatch(file):
                return 'Invalid account', 400

            if os.path.exists(os.path.join(CONFIG_PATH, file) + '.json'):
                return 'Account exists', 200
            else:
                return 'Account does not exists', 400

        @self.app.route('/api/do_task', methods= ['GET'])
        @HttpServer.wrapaccount()
        async def do_task(mgr: Account):
            if self.qq_only:
                return 'Please use in group', 400
            try:
                return await mgr.do_daily(), 200
            except Exception as e:
                return str(e), 502

        @self.app.route('/api/tools', methods = ['GET'])
        @HttpServer.wrapaccount(readonly = True)
        async def get_tools_info(mgr: Account):
            return mgr.generate_tools_info()

        @self.app.route('/api/do_single', methods = ['POST'])
        @HttpServer.wrapaccount()
        async def do_single(mgr: Account):
            data = await request.get_json()
            config = data['config']
            module = data['order'] # list
            try:
                return await mgr.do_from_key(config, module), 200
            except Exception as e:
                return str(e), 502

        @self.app.route('/api/validate', methods = ['POST'])
        async def validate():
            data = await request.get_json()
            from ..bsdk.validator import validate_ok_dict
            if 'id' not in data:
                return "incorrect", 403
            id = data['id']
            validate_ok_dict[id] = data
            return "", 200

        @self.app.route('/api/query_validate', methods = ['GET'])
        @HttpServer.wrapaccount(readonly = True)
        async def query_validate(mgr: Account):
            from ..bsdk.validator import validate_dict
            if mgr.username not in validate_dict:
                return "empty", 404
            elif validate_dict[mgr.username] == "ok":
                del validate_dict[mgr.username]
                return "ok", 200
            else:
                url = validate_dict[mgr.username]
                del validate_dict[mgr.username]
                return url, 401

        # frontend
        @self.app.route('/', methods = ['GET'])
        async def index():
            return await render_template('index.html')
        
        @self.app.route('/config.html', methods = ['GET'])
        async def config():
            return await render_template('config.html', url="info")

        @self.app.route('/info.html', methods = ['GET'])
        async def tools():
            return await render_template('info.html', url="tools")
        
        @self.app.route('/action.html', methods = ['GET'])
        async def action():
            return await render_template('action.html', url="config")

        @self.app.route('/geetest.html', methods = ['GET'])
        async def geetest():
            return await render_template('geetest.html')

    def run_forever(self, loop):
        self.quart.register_blueprint(self.app)
        self.quart.run(host=self.host, port=self.port, loop=loop)
    
