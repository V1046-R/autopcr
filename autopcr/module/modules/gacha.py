from ...model.custom import GachaReward
from ..modulebase import *
from ..config import *
from ...core.pcrclient import pcrclient
from ...model.error import *
from ...db.database import db
from ...model.enums import *
import datetime
from collections import Counter

@description('扭曲装备扭蛋')
@name('普通扭蛋')
@default(True)
class normal_gacha(Module):
    async def do_task(self, client: pcrclient):
        resp = await client.get_gacha_index()
        normal_gacha: GachaParameter = None
        for gacha in resp.gacha_info:
            if gacha.type == eGachaType.FreeOnly and gacha.cost_num_single == 0:
                normal_gacha = gacha 
                break
        if normal_gacha.free_exec_times != 0:
            raise SkipError("已进行过普通扭蛋")
        resp = await client.exec_gacha(normal_gacha.id, 10, 0, eGachaDrawType.Free, -1, 0)
        memory = [i for i in resp.reward_info_list if db.is_unit_memory((i.type, i.id))]
        msg = "10件装备"
        if memory:
            msg = await client.serlize_reward(memory) + f"\n{10 - len(memory)}件装备"
        self._log(msg)

@description('有免费十连时自动抽取')
@name('免费十连')
@default(False)
class free_gacha(Module):
    async def do_task(self, client: pcrclient):
        res = await client.get_gacha_index()
        if res.campaign_info is None:
            raise SkipError("免费十连已结束")
        schedule = db.campaign_gacha[res.campaign_info.campaign_id]
        gacha_list = db.free_gacha_list[schedule.campaign_id]
        start_time = db.parse_time(schedule.start_time)
        end_time = db.parse_time(schedule.end_time)
        if datetime.datetime.now() >= end_time:
            raise SkipError("免费十连已结束")
        if datetime.datetime.now() < start_time:
            raise SkipError("免费十连尚未开始")
        if res.campaign_info.fg10_exec_cnt == 0:
            raise SkipError("今日份免费十连已使用")
        cnt = res.campaign_info.fg10_exec_cnt
        gacha_list = set(gacha.gacha_id for gacha in gacha_list)
        for gacha_info in res.gacha_info:
            if gacha_info.id in gacha_list:
                target_gacha = gacha_info
                break
        else:
            raise ValueError("target gacha not found")

        gacha_reward: GachaReward = GachaReward()

        while cnt > 0:
            gacha_reward += await client.exec_gacha_aware(target_gacha, 10, eGachaDrawType.Campaign10Shot, cnt, res.campaign_info.campaign_id)
            cnt -= 1

        self._log(await client.serlize_gacha_reward(gacha_reward))
