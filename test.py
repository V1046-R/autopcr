import asyncio
from autopcr.modulebase import ModuleManager
from autopcr.modules import register_test

register_test()
mgr = ModuleManager('test.json')
print(asyncio.run(mgr.do_task()))