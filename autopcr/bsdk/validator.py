from ..util import aiorequests, questutils
from json import loads
import asyncio

validate_dict = {}
validate_ok_dict = {}

async def manualValidator(account, gt, challenge, userid):
    id = questutils.create_quest_token()
    url = f"/daily/geetest.html?id={id}&captcha_type=1&challenge={challenge}&gt={gt}&userid={userid}&gs=1"
    validate_dict[account] = url
    for _ in range(120):
        if id not in validate_ok_dict:
            await asyncio.sleep(1)
        else:
            info = {
                "challenge": validate_ok_dict[id]['challenge'], 
                "gt_user_id": validate_ok_dict[id]['userid'], 
                "validate" : validate_ok_dict[id]['validate'], 
            }
            del validate_ok_dict[id]
            break
    else:
        raise ValueError("验证码验证超时")

    return info

async def autoValidator(account, gt, challenge, userid):
    url = f"https://pcrd.tencentbot.top/geetest_renew"
    header = {"Content-Type": "application/json", "User-Agent": "autopcr/1.0.0"}
    info = ""
    print(f"farm: Auto verifying")
    ret = None
    try:
        res = await aiorequests.get(url=url, headers=header)
        res.raise_for_status()
        res = await res.content
        res = loads(res)
        uuid = res["uuid"]
        msg = [f"uuid={uuid}"]
        ccnt = 0
        while ccnt < 10:
            ccnt += 1
            res = await aiorequests.get(url=f"https://pcrd.tencentbot.top/check/{uuid}", headers=header)
            res.raise_for_status()
            res = await res.content
            res = loads(res)
            if "queue_num" in res:
                nu = res["queue_num"]
                msg.append(f"queue_num={nu}")
                tim = min(int(nu), 3) * 10
                msg.append(f"sleep={tim}")
                print(f"farm:\n" + "\n".join(msg))
                msg = []
                print(f'farm: {uuid} in queue, sleep {tim} seconds')
                await asyncio.sleep(tim)
            else:
                info = res["info"]
                if info in ["fail", "url invalid"]:
                    raise Exception("Captcha failed")
                elif info == "in running":
                    await asyncio.sleep(8)
                elif 'validate' in info:
                    ret = info
            if ccnt >= 10:
                raise Exception("Captcha failed")
    except:
        if not ret: ret = await manualValidator(account, gt, challenge, userid)

    return ret
