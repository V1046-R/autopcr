#type: ignore
from typing import List
from .modelbase import Request
from .responses import *
from .common import *
from .enums import *

class UniqueEquipMultiEnhanceRequest(Request[UniqueEquipMultiEnhanceResponse]):
	unit_id: int = None
	slot_id: int = None
	current_gold: int = None
	craft_equip_recipe: List[EnhanceRecipe] = None
	craft_item_recepe: List[EnhanceRecipe] = None
	rankup_equip_recipe: List[EnhanceRecipe] = None
	rankup_item_recipe: List[EnhanceRecipe] = None
	rankup_potion_recipe: List[EnhanceRecipe] = None
	current_rank: int = None
	after_rank: int = None
	enhancement_item_list: List[EnhanceRecipe] = None
	current_enhancement_pt: int = None
	@property
	def url(self) -> str:
		return "equipment/multi_enhance_unique"
class ArcadeTopRequest(Request[ArcadeTopResponse]):
	@property
	def url(self) -> str:
		return "arcade/top"
	pass
class ArcadeBuyRequest(Request[ArcadeBuyResponse]):
	arcade_id: int = None
	room_coin: int = None
	@property
	def url(self) -> str:
		return "arcade/buy"
class ArcadeSyncStoryListRequest(Request[ArcadeSyncStoryListResponse]):
	arcade_id: int = None
	story_id_list: List[int] = None
	@property
	def url(self) -> str:
		return "arcade/sync_story_list"
class ArcadeStoryListRequest(Request[ArcadeStoryListResponse]):
	arcade_id: int = None
	@property
	def url(self) -> str:
		return "arcade/story_list"
class ArcadeReadStoryRequest(Request[ArcadeReadStoryResponse]):
	story_id: int = None
	@property
	def url(self) -> str:
		return "arcade/read_story"
class ArenaInfoRequest(Request[ArenaInfoResponse]):
	@property
	def url(self) -> str:
		return "arena/info"
	pass
class ArenaSearchRequest(Request[ArenaSearchResponse]):
	@property
	def url(self) -> str:
		return "arena/search"
	pass
class ArenaApplyRequest(Request[ArenaApplyResponse]):
	battle_viewer_id: int = None
	opponent_rank: int = None
	@property
	def url(self) -> str:
		return "arena/apply"
class ArenaCancelRequest(Request[ArenaCancelResponse]):
	battle_viewer_id: int = None
	@property
	def url(self) -> str:
		return "arena/cancel"
class ArenaStartRequest(Request[ArenaStartResponse]):
	token: str = None
	battle_viewer_id: int = None
	remain_battle_number: int = None
	disable_skin: int = None
	battle_id: int = None
	arena_wave_result_list: List[ArenaWaveResult] = None
	is_skipped: int = None
	@property
	def url(self) -> str:
		return "arena/start"
class ArenaIntervalCancelRequest(Request[ArenaIntervalCancelResponse]):
	@property
	def url(self) -> str:
		return "arena/interval_cancel"
class ArenaResetBattleNumberRequest(Request[ArenaResetBattleNumberResponse]):
	@property
	def url(self) -> str:
		return "arena/reset_battle_number"
	pass
class ArenaRankingRequest(Request[ArenaRankingResponse]):
	limit: int = None
	page: int = None
	@property
	def url(self) -> str:
		return "arena/ranking"
class ArenaHistoryRequest(Request[ArenaHistoryResponse]):
	@property
	def url(self) -> str:
		return "arena/history"
	pass
class ArenaHistoryDetailRequest(Request[ArenaHistoryDetailResponse]):
	log_id: int = None
	@property
	def url(self) -> str:
		return "arena/history_detail"
class ArenaReplayRequest(Request[ArenaReplayResponse]):
	log_id: int = None
	@property
	def url(self) -> str:
		return "arena/replay"
class ArenaMoveGroupRequest(Request[ArenaMoveGroupResponse]):
	group_id: int = None
	@property
	def url(self) -> str:
		return "arena/move_group"
class ArenaHistoryDamageRankingRequest(Request[ArenaHistoryDamageRankingResponse]):
	log_id: int = None
	@property
	def url(self) -> str:
		return "arena/history_damage_ranking"
class ArenaTimeRewardAcceptRequest(Request[ArenaTimeRewardAcceptResponse]):
	@property
	def url(self) -> str:
		return "arena/time_reward_accept"
	pass
class CharaETicketRewardsRequest(Request[CharaETicketRewardsResponse]):
	ticket_id: int = None
	@property
	def url(self) -> str:
		return "chara_e_ticket/rewards"
class CharaETicketExchangeRequest(Request[CharaETicketExchangeResponse]):
	ticket_id: int = None
	ticket_count: int = None
	unit_id: int = None
	@property
	def url(self) -> str:
		return "chara_e_ticket/exchange"
class CheckAgreementRequest(Request[CheckAgreementResponse]):
	@property
	def url(self) -> str:
		return "check/check_agreement"
	pass
class AcceptAgreementRequest(Request[AcceptAgreementResponse]):
	agreement_type: int = None
	agreement_ver: int = None
	policy_ver: int = None
	@property
	def url(self) -> str:
		return "check/accept_agreement"
class ClanBattleBossHistoryRequest(Request[ClanBattleBossHistoryResponse]):
	clan_id: int = None
	clan_battle_id: int = None
	period: int = None
	page: int = None
	@property
	def url(self) -> str:
		return "clan_battle/boss_history"
class ClanBattleBossInfoRequest(Request[ClanBattleBossInfoResponse]):
	clan_id: int = None
	clan_battle_id: int = None
	lap_num: int = None
	order_num: int = None
	@property
	def url(self) -> str:
		return "clan_battle/boss_info"
class ClanBattleDamageReportRequest(Request[ClanBattleDamageReportResponse]):
	clan_id: int = None
	clan_battle_id: int = None
	lap_num: int = None
	order_num: int = None
	@property
	def url(self) -> str:
		return "clan_battle/damage_report"
class ClanBattleFinishRequest(Request[ClanBattleFinishResponse]):
	clan_id: int = None
	clan_battle_id: int = None
	lap_num: int = None
	order_num: int = None
	user_unit: ClanBattleFinishUnit = None
	boss_hp: int = None
	boss_damage: int = None
	remain_time: int = None
	total_damage: int = None
	battle_log_id: int = None
	is_auto: int = None
	@property
	def url(self) -> str:
		return "clan_battle/finish"
class ClanBattlePeriodRankingRequest(Request[ClanBattlePeriodRankingResponse]):
	clan_id: int = None
	clan_battle_id: int = None
	period: int = None
	month: int = None
	page: int = None
	is_my_clan: int = None
	is_first: int = None
	@property
	def url(self) -> str:
		return "clan_battle/period_ranking"
class ClanBattleBossRankingInClanRequest(Request[ClanBattleBossRankingInClanResponse]):
	clan_id: int = None
	clan_battle_id: int = None
	month: int = None
	@property
	def url(self) -> str:
		return "clan_battle/boss_ranking_in_clan"
class ClanBattleResetHpRequest(Request[ClanBattleResetHpResponse]):
	hp_reset_count: int = None
	current_currency_num: int = None
	@property
	def url(self) -> str:
		return "clan_battle/reset_hp"
class ClanBattleStartRequest(Request[ClanBattleStartResponse]):
	clan_id: int = None
	clan_battle_id: int = None
	period: int = None
	lap_num: int = None
	order_num: int = None
	owner_viewer_id: int = None
	support_unit_id: int = None
	support_battle_rarity: int = None
	remaining_count: int = None
	@property
	def url(self) -> str:
		return "clan_battle/start"
class ClanBattleSupportUnitListRequest(Request[ClanBattleSupportUnitListResponse]):
	clan_id: int = None
	@property
	def url(self) -> str:
		return "clan_battle/support_unit_list"
class ClanBattleSupportUnitList2Request(Request[ClanBattleSupportUnitList2Response]):
	clan_id: int = None
	@property
	def url(self) -> str:
		return "clan_battle/support_unit_list_2"
class ClanBattleTopRequest(Request[ClanBattleTopResponse]):
	clan_id: int = None
	is_first: int = None
	current_clan_battle_coin: int = None
	@property
	def url(self) -> str:
		return "clan_battle/top"
class ClanBattleHistoryReportRequest(Request[ClanBattleHistoryReportResponse]):
	clan_id: int = None
	history_id: int = None
	@property
	def url(self) -> str:
		return "clan_battle/history_report"
class ClanBattleRehearsalStartRequest(Request[ClanBattleRehearsalStartResponse]):
	clan_id: int = None
	clan_battle_id: int = None
	period: int = None
	lap_num: int = None
	order_num: int = None
	owner_viewer_id: int = None
	support_unit_id: int = None
	support_battle_rarity: int = None
	is_actual_boss_status: int = None
	@property
	def url(self) -> str:
		return "clan_battle/rehearsal_start"
class ClanBattleRehearsalFinishRequest(Request[ClanBattleRehearsalFinishResponse]):
	clan_id: int = None
	clan_battle_id: int = None
	lap_num: int = None
	order_num: int = None
	user_unit: ClanBattleFinishUnit = None
	boss_hp: int = None
	boss_damage: int = None
	remain_time: int = None
	total_damage: int = None
	battle_log_id: int = None
	is_actual_boss_status: int = None
	@property
	def url(self) -> str:
		return "clan_battle/rehearsal_finish"
class ClanBattleReloadDetailInfoRequest(Request[ClanBattleReloadDetailInfoResponse]):
	clan_id: int = None
	clan_battle_id: int = None
	lap_num: int = None
	order_num: int = None
	@property
	def url(self) -> str:
		return "clan_battle/reload_detail_info"
class ClanBattleMyLogRequest(Request[ClanBattleMyLogResponse]):
	clan_id: int = None
	@property
	def url(self) -> str:
		return "clan_battle/mylog"
class ClanBattleDeleteRehearsalMyLogRequest(Request[ClanBattleDeleteRehearsalMyLogResponse]):
	clan_id: int = None
	mylog_id: int = None
	@property
	def url(self) -> str:
		return "clan_battle/delete_rehearsal_mylog"
class ClanBattleSaveRehearsalMyLogRequest(Request[ClanBattleSaveRehearsalMyLogResponse]):
	clan_id: int = None
	mylog_id: int = None
	lap_num: int = None
	order_num: int = None
	user_unit: List[UnitDamageInfo] = None
	total_damage: int = None
	boss_damage: int = None
	battle_log_id: int = None
	is_auto: int = None
	@property
	def url(self) -> str:
		return "clan_battle/save_rehearsal_mylog"
class ClanBattleConfirmRehearsalMyLogRequest(Request[ClanBattleConfirmRehearsalMyLogResponse]):
	clan_id: int = None
	@property
	def url(self) -> str:
		return "clan_battle/confirm_rehearsal_mylog"
class ClanBattleMyLogDetailRequest(Request[ClanBattleMyLogDetailResponse]):
	clan_id: int = None
	clan_battle_id: int = None
	@property
	def url(self) -> str:
		return "clan_battle/mylog_detail"
class ClanBattleDeleteTrainingMyLogRequest(Request[ClanBattleDeleteTrainingMyLogResponse]):
	mylog_id: int = None
	@property
	def url(self) -> str:
		return "clan_battle/delete_training_mylog"
class ClanBattleSaveTrainingMyLogRequest(Request[ClanBattleSaveTrainingMyLogResponse]):
	clan_id: int = None
	training_id: int = None
	mylog_id: int = None
	clan_battle_mode: int = None
	phase: int = None
	order_num: int = None
	user_unit: List[UnitDamageInfo] = None
	total_damage: int = None
	boss_damage: int = None
	battle_log_id: int = None
	is_auto: int = None
	@property
	def url(self) -> str:
		return "clan_battle/save_training_mylog"
class ClanBattleConfirmTrainingMyLogRequest(Request[ClanBattleConfirmTrainingMyLogResponse]):
	@property
	def url(self) -> str:
		return "clan_battle/confirm_training_my_log"
class ClanBattleTrainingStartRequest(Request[ClanBattleTrainingStartResponse]):
	clan_id: int = None
	training_id: int = None
	clan_battle_mode: int = None
	phase: int = None
	order_num: int = None
	owner_viewer_id: int = None
	support_unit_id: int = None
	support_battle_rarity: int = None
	@property
	def url(self) -> str:
		return "clan_battle/training_start"
class ClanBattleTrainingFinishRequest(Request[ClanBattleTrainingFinishResponse]):
	clan_id: int = None
	training_id: int = None
	clan_battle_mode: int = None
	phase: int = None
	order_num: int = None
	user_unit: ClanBattleFinishUnit = None
	boss_hp: int = None
	boss_damage: int = None
	remain_time: int = None
	total_damage: int = None
	battle_log_id: int = None
	is_auto: int = None
	@property
	def url(self) -> str:
		return "clan_battle/training_finish"
class ClanBattleMissionIndexRequest(Request[ClanBattleMissionIndexResponse]):
	@property
	def url(self) -> str:
		return "clan_battle/mission_index"
	pass
class ClanBattleSuggestDeckListRequest(Request[ClanBattleSuggestDeckListResponse]):
	recommend_group: int = None
	clan_battle_id: int = None
	lap_num: int = None
	order_num: int = None
	@property
	def url(self) -> str:
		return "clan_battle/suggest_deck_list"
class ClanBattleSuggestDeckReplayRequest(Request[ClanBattleSuggestDeckReplayResponse]):
	clan_battle_id: int = None
	enc_key: str = None
	@property
	def url(self) -> str:
		return "clan_battle/suggest_deck_replay"
class ClanBattleSuggestDeckReplayReportRequest(Request[ClanBattleSuggestDeckReplayReportResponse]):
	clan_battle_id: int = None
	report_key: str = None
	@property
	def url(self) -> str:
		return "clan_battle/suggest_deck_replay_report"
class ClanDetailRequest(Request[ClanDetailResponse]):
	clan_id: int = None
	page: int = None
	@property
	def url(self) -> str:
		return "clan/detail"
class ClanInviteRequest(Request[ClanInviteResponse]):
	invited_viewer_id: int = None
	invite_message: str = None
	@property
	def url(self) -> str:
		return "clan/invite"
class ClanInviteCancelRequest(Request[ClanInviteCancelResponse]):
	invite_id: int = None
	@property
	def url(self) -> str:
		return "clan/cancel_invite"
class ClanInviteBlockRequest(Request[ClanInviteBlockResponse]):
	invite_id: int = None
	@property
	def url(self) -> str:
		return "clan/block_invite"
class ClanInviteUnblockRequest(Request[ClanInviteUnblockResponse]):
	block_id: int = None
	@property
	def url(self) -> str:
		return "clan/cancel_block_invite"
class ClanInviteRejectRequest(Request[ClanInviteRejectResponse]):
	invite_id: int = None
	@property
	def url(self) -> str:
		return "clan/reject_invite"
class UserInviteClanListRequest(Request[UserInviteClanListResponse]):
	page: int = None
	@property
	def url(self) -> str:
		return "clan/invited_clan_list"
class ClanInvitedUserListRequest(Request[ClanInvitedUserListResponse]):
	clan_id: int = None
	page: int = None
	oldest_time: int = None
	@property
	def url(self) -> str:
		return "clan/invite_user_list"
class ClanBlockListRequest(Request[ClanBlockListResponse]):
	page: int = None
	@property
	def url(self) -> str:
		return "clan/block_list"
class ClanInvitePermissionRequest(Request[ClanInvitePermissionResponse]):
	invite_accept_flag: int = None
	@property
	def url(self) -> str:
		return "clan/update_invite_accept_flag"
class ClanInfoRequest(Request[ClanInfoResponse]):
	clan_id: int = None
	get_user_equip: int = None
	@property
	def url(self) -> str:
		return "clan/info"
class OtherClanInfoRequest(Request[OtherClanInfoResponse]):
	clan_id: int = None
	@property
	def url(self) -> str:
		return "clan/others_info"
class ClanCreateRequest(Request[ClanCreateResponse]):
	clan_name: str = None
	description: str = None
	join_condition: int = None
	activity: int = None
	clan_battle_mode: int = None
	@property
	def url(self) -> str:
		return "clan/create"
class ClanUpdateRequest(Request[ClanUpdateResponse]):
	clan_id: int = None
	clan_name: str = None
	description: str = None
	join_condition: int = None
	activity: int = None
	clan_battle_mode: int = None
	@property
	def url(self) -> str:
		return "clan/update"
class ClanBreakUpRequest(Request[ClanBreakUpResponse]):
	clan_id: int = None
	@property
	def url(self) -> str:
		return "clan/breakup"
class ClanJoinRequest(Request[ClanJoinResponse]):
	clan_id: int = None
	from_invite: int = None
	@property
	def url(self) -> str:
		return "clan/join"
class ClanLeaveRequest(Request[ClanLeaveResponse]):
	clan_id: int = None
	@property
	def url(self) -> str:
		return "clan/leave"
class ClanRemoveRequest(Request[ClanRemoveResponse]):
	clan_id: int = None
	remove_viewer_id: int = None
	@property
	def url(self) -> str:
		return "clan/remove"
class ClanSearchRequest(Request[ClanSearchResponse]):
	clan_name: str = None
	join_condition: int = None
	member_condition_range: int = None
	activity: int = None
	clan_battle_mode: int = None
	@property
	def url(self) -> str:
		return "clan/search_clan"
class ClanSearchUserRequest(Request[ClanSearchUserResponse]):
	level_group_id: int = None
	@property
	def url(self) -> str:
		return "clan/search_user"
class ClanJoinRequestListRequest(Request[ClanJoinRequestListResponse]):
	clan_id: int = None
	page: int = None
	oldest_time: int = None
	@property
	def url(self) -> str:
		return "clan/join_request_list"
class ClanJoinRequestCancelRequest(Request[ClanJoinRequestCancelResponse]):
	clan_id: int = None
	@property
	def url(self) -> str:
		return "clan/join_request_cancel"
class ClanJoinRequestAcceptRequest(Request[ClanJoinRequestAcceptResponse]):
	request_viewer_id: int = None
	clan_id: int = None
	@property
	def url(self) -> str:
		return "clan/join_request_accept"
class ClanJoinRequestRejectRequest(Request[ClanJoinRequestRejectResponse]):
	request_viewer_id: int = None
	clan_id: int = None
	@property
	def url(self) -> str:
		return "clan/join_request_reject"
class ClanSetDispatchStatusRequest(Request[ClanSetDispatchStatusResponse]):
	clan_id: int = None
	unit_id: int = None
	position: int = None
	action: int = None
	@property
	def url(self) -> str:
		return "clan/set_dispatch_status"
class ChangeRoleRequest(Request[ChangeRoleResponse]):
	role_info: List[RoleInfo] = None
	@property
	def url(self) -> str:
		return "clan/change_role"
class ClanChatRequest(Request[ClanChatResponse]):
	clan_id: int = None
	type: int = None
	message: str = None
	@property
	def url(self) -> str:
		return "clan/chat"
class ClanDamageReportRequest(Request[ClanDamageReportResponse]):
	target_viewer_id: int = None
	clan_id: int = None
	battle_type: int = None
	battle_log_id: int = None
	@property
	def url(self) -> str:
		return "clan/chat_damage_report"
class ClanChatInfoListRequest(Request[ClanChatInfoListResponse]):
	clan_id: int = None
	start_message_id: int = None
	search_date: str = None
	direction: int = None
	count: int = None
	wait_interval: int = None
	update_message_ids: List[int] = None
	@property
	def url(self) -> str:
		return "clan/chat_info_list"
class ClanLikeRequest(Request[ClanLikeResponse]):
	clan_id: int = None
	target_viewer_id: int = None
	@property
	def url(self) -> str:
		return "clan/like"
class CheckExistClanRequest(Request[CheckExistClanResponse]):
	@property
	def url(self) -> str:
		return "check/exist_clan"
class ClanMemberBattleStartRequest(Request[ClanMemberBattleStartResponse]):
	battle_viewer_id: int = None
	unit_id_list: List[int] = None
	disable_skin: int = None
	create_time: int = None
	@property
	def url(self) -> str:
		return "clan/clan_member_battle_start"
class ClanMemberBattleFinishRequest(Request[ClanMemberBattleFinishResponse]):
	battle_id: int = None
	wave_result_list: List[FriendBattleResult] = None
	@property
	def url(self) -> str:
		return "clan/clan_member_battle_finish"
class DeckUpdateRequest(Request[DeckUpdateResponse]):
	deck_number: int = None
	unit_id_1: int = None
	unit_id_2: int = None
	unit_id_3: int = None
	unit_id_4: int = None
	unit_id_5: int = None
	@property
	def url(self) -> str:
		return "deck/update"
class DeckUpdateListRequest(Request[DeckUpdateListResponse]):
	deck_list: List[DeckListData] = None
	@property
	def url(self) -> str:
		return "deck/update_list"
class DungeonInfoRequest(Request[DungeonInfoResponse]):
	@property
	def url(self) -> str:
		return "dungeon/info"
	pass
class DungeonEnterAreaRequest(Request[DungeonEnterAreaResponse]):
	dungeon_area_id: int = None
	@property
	def url(self) -> str:
		return "dungeon/enter_area"
class DungeonClanDispatchUnitListRequest(Request[DungeonClanDispatchUnitListResponse]):
	dungeon_area_id: int = None
	@property
	def url(self) -> str:
		return "dungeon/clan_dispatch_unit_list"
class DungeonDispatchUnitList2Request(Request[DungeonDispatchUnitList2Response]):
	dungeon_area_id: int = None
	@property
	def url(self) -> str:
		return "dungeon/dispatch_unit_list_2"
class DungeonBattleStartRequest(Request[DungeonBattleStartResponse]):
	quest_id: int = None
	unit_list: List[DungeonBattleStartUnit] = None
	disable_skin: int = None
	support_battle_rarity: int = None
	@property
	def url(self) -> str:
		return "dungeon/battle_start"
class DungeonBattleFinishRequest(Request[DungeonBattleFinishResponse]):
	quest_id: int = None
	user_unit: List[DungeonQueryUnit] = None
	versus_user_unit: List[DungeonQueryUnit] = None
	remain_time: int = None
	total_damage: int = None
	@property
	def url(self) -> str:
		return "dungeon/battle_finish"
class DungeonResetRequest(Request[DungeonResetResponse]):
	dungeon_area_id: int = None
	@property
	def url(self) -> str:
		return "dungeon/reset"
class DungeonBattleRetireRequest(Request[DungeonBattleRetireResponse]):
	quest_id: int = None
	@property
	def url(self) -> str:
		return "dungeon/battle_retire"
class DungeonSkipRequest(Request[DungeonSkipResponse]):
	dungeon_area_id: int = None
	@property
	def url(self) -> str:
		return "dungeon/skip"
class EmblemTopRequest(Request[EmblemTopResponse]):
	@property
	def url(self) -> str:
		return "emblem/top"
	pass
class EmblemChangeRequest(Request[EmblemChangeResponse]):
	emblem_id: int = None
	@property
	def url(self) -> str:
		return "emblem/change"
class AutomaticEquipEnhanceRequest(Request[AutomaticEquipEnhanceResponse]):
	unit_id: int = None
	equip_slot_num: int = None
	current_enhancement_pt: int = None
	item_list: List[InventoryInfoPost] = None
	buy_item_list: List[ShopBuyInfo] = None
	@property
	def url(self) -> str:
		return "equipment/automatic_enhance"
class AutomaticEquipEnhanceUniqueRequest(Request[AutomaticEquipEnhanceUniqueResponse]):
	unit_id: int = None
	equip_slot_num: int = None
	current_enhancement_pt: int = None
	item_list: List[InventoryInfoPost] = None
	buy_item_list: List[ShopBuyInfo] = None
	@property
	def url(self) -> str:
		return "equipment/automatic_enhance_unique"
class EquipEnhanceRequest(Request[EquipEnhanceResponse]):
	unit_id: int = None
	equip_slot_num: int = None
	item_list: List[InventoryInfoPost] = None
	current_enhancement_pt: int = None
	@property
	def url(self) -> str:
		return "equipment/enhance"
class UniqueEquipEnhanceRequest(Request[UniqueEquipEnhanceResponse]):
	unit_id: int = None
	equip_slot_num: int = None
	item_list: List[InventoryInfoPost] = None
	current_enhancement_pt: int = None
	@property
	def url(self) -> str:
		return "equipment/enhance_unique"
class EquipEnhanceMaxRequest(Request[EquipEnhanceMaxResponse]):
	unit_id: int = None
	equip_slot_num: int = None
	@property
	def url(self) -> str:
		return "equipment/enhance_max"
class EquipRequestRequest(Request[EquipRequestResponse]):
	equip_id: int = None
	clan_id: int = None
	@property
	def url(self) -> str:
		return "equipment/request"
class EquipDonateRequest(Request[EquipDonateResponse]):
	clan_id: int = None
	message_id: int = None
	donation_num: int = None
	current_equip_num: int = None
	@property
	def url(self) -> str:
		return "equipment/donate"
class EquipCraftRequest(Request[EquipCraftResponse]):
	equip_id: int = None
	equip_recipe_list: List[UserEquipParameterIdCount] = None
	current_equip_num: int = None
	@property
	def url(self) -> str:
		return "equipment/craft"
class UniqueEquipCraftRequest(Request[UniqueEquipCraftResponse]):
	equip_id: int = None
	equip_recipe_list: List[UserEquipParameterIdCount] = None
	item_recipe_list: List[UserEquipParameterIdCount] = None
	current_equip_num: int = None
	@property
	def url(self) -> str:
		return "equipment/craft_unique"
class UniqueEquipRankupRequest(Request[UniqueEquipRankupResponse]):
	unit_id: int = None
	equip_slot_num: int = None
	equip_recipe_list: List[UserEquipParameterIdCount] = None
	item_recipe_list: List[UserEquipParameterIdCount] = None
	current_rank: int = None
	@property
	def url(self) -> str:
		return "equipment/rankup_unique"
class EquipGetRequestRequest(Request[EquipGetRequestResponse]):
	clan_id: int = None
	message_id: int = None
	@property
	def url(self) -> str:
		return "equipment/get_request"
class EquipmentFreeEnhanceRequest(Request[EquipmentFreeEnhanceResponse]):
	unit_id: int = None
	equip_slot_num: int = None
	after_equip_level: int = None
	@property
	def url(self) -> str:
		return "equipment/free_enhance"
class EventGachaIndexRequest(Request[EventGachaIndexResponse]):
	event_id: int = None
	gacha_id: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/gacha_index"
class EventGachaExecRequest(Request[EventGachaExecResponse]):
	event_id: int = None
	gacha_id: int = None
	gacha_times: int = None
	current_cost_num: int = None
	loop_box_multi_gacha_flag: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/gacha_exec"
class EventGachaResetRequest(Request[EventGachaResetResponse]):
	event_id: int = None
	gacha_id: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/gacha_reset"
class EventGachaLineupRequest(Request[EventGachaLineupResponse]):
	event_id: int = None
	gacha_id: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/gacha_lineup"
class FkeTopRequest(Request[FkeTopResponse]):
	@property
	def url(self) -> str:
		return "fke/top"
	pass
class FkeSyncTopRequest(Request[FkeSyncTopResponse]):
	happening_id_list: List[int] = None
	@property
	def url(self) -> str:
		return "fke/sync_top"
class FkeStartRequest(Request[FkeStartResponse]):
	@property
	def url(self) -> str:
		return "fke/start"
	pass
class FkeFinishRequest(Request[FkeFinishResponse]):
	fke_play_id: int = None
	base_fke_point: int = None
	happening_id_list: List[int] = None
	@property
	def url(self) -> str:
		return "fke/finish"
class FriendAcceptRequest(Request[FriendAcceptResponse]):
	target_viewer_id: int = None
	@property
	def url(self) -> str:
		return "friend/accept"
class FriendCancelRequest(Request[FriendCancelResponse]):
	target_viewer_id: int = None
	@property
	def url(self) -> str:
		return "friend/cancel"
class FriendFriendListRequest(Request[FriendFriendListResponse]):
	@property
	def url(self) -> str:
		return "friend/friend_list"
	pass
class FriendPendingListRequest(Request[FriendPendingListResponse]):
	@property
	def url(self) -> str:
		return "friend/pending_list"
	pass
class FriendRejectRequest(Request[FriendRejectResponse]):
	target_viewer_id: int = None
	@property
	def url(self) -> str:
		return "friend/reject"
class FriendRemoveRequest(Request[FriendRemoveResponse]):
	target_viewer_id: int = None
	@property
	def url(self) -> str:
		return "friend/remove"
class FriendRequestRequest(Request[FriendRequestResponse]):
	target_viewer_id: int = None
	@property
	def url(self) -> str:
		return "friend/request"
class FriendRequestListRequest(Request[FriendRequestListResponse]):
	@property
	def url(self) -> str:
		return "friend/request_list"
	pass
class FriendSearchRequest(Request[FriendSearchResponse]):
	level_group_id: int = None
	@property
	def url(self) -> str:
		return "friend/search"
class FriendMissionIndexRequest(Request[FriendMissionIndexResponse]):
	campaign_id: int = None
	@property
	def url(self) -> str:
		return "friend/mission_index"
class FriendMissionAcceptRequest(Request[FriendMissionAcceptResponse]):
	campaign_id: int = None
	type: int = None
	id: int = None
	@property
	def url(self) -> str:
		return "friend/mission_accept"
class FriendGetMissionTargetFriendCountRequest(Request[FriendGetMissionTargetFriendCountResponse]):
	campaign_id: int = None
	mission_id: int = None
	@property
	def url(self) -> str:
		return "friend/get_mission_target_friend_count"
class GachaIndexRequest(Request[GachaIndexResponse]):
	@property
	def url(self) -> str:
		return "gacha/index"
	pass
class GachaExecRequest(Request[GachaExecResponse]):
	gacha_id: int = None
	gacha_times: int = None
	exchange_id: int = None
	draw_type: int = None
	current_cost_num: int = None
	campaign_id: int = None
	@property
	def url(self) -> str:
		return "gacha/exec"
class GachaExchangePointRequest(Request[GachaExchangePointResponse]):
	exchange_id: int = None
	unit_id: int = None
	current_point: int = None
	@property
	def url(self) -> str:
		return "gacha/exchange_point"
class GachaPrizeHistoryRequest(Request[GachaPrizeHistoryResponse]):
	gacha_id: int = None
	offset: int = None
	page: int = None
	@property
	def url(self) -> str:
		return "gacha/prize_history"
class GachaSelectPrizeRequest(Request[GachaSelectPrizeResponse]):
	prizegacha_id: int = None
	item_id: int = None
	@property
	def url(self) -> str:
		return "gacha/select_prize"
class GachaPrizeRewardRequest(Request[GachaPrizeRewardResponse]):
	gacha_id: int = None
	@property
	def url(self) -> str:
		return "gacha/prize_reward"
class GachaSpecialFesIndexRequest(Request[GachaSpecialFesIndexResponse]):
	@property
	def url(self) -> str:
		return "gacha/special_fes_index"
class GrandArenaInfoRequest(Request[GrandArenaInfoResponse]):
	@property
	def url(self) -> str:
		return "grand_arena/info"
	pass
class GrandArenaSearchRequest(Request[GrandArenaSearchResponse]):
	@property
	def url(self) -> str:
		return "grand_arena/search"
	pass
class GrandArenaApplyRequest(Request[GrandArenaApplyResponse]):
	battle_viewer_id: int = None
	opponent_rank: int = None
	@property
	def url(self) -> str:
		return "grand_arena/apply"
class GrandArenaCancelRequest(Request[GrandArenaCancelResponse]):
	battle_viewer_id: int = None
	@property
	def url(self) -> str:
		return "grand_arena/cancel"
class GrandArenaStartRequest(Request[GrandArenaStartResponse]):
	token: str = None
	battle_viewer_id: int = None
	remain_battle_number: int = None
	disable_skin: int = None
	@property
	def url(self) -> str:
		return "grand_arena/start"
class GrandArenaFinishRequest(Request[GrandArenaFinishResponse]):
	battle_id: int = None
	arena_wave_result_list: List[ArenaWaveResult] = None
	is_skipped: int = None
	@property
	def url(self) -> str:
		return "grand_arena/finish"
class GrandArenaCancelIntervalRequest(Request[GrandArenaCancelIntervalResponse]):
	@property
	def url(self) -> str:
		return "grand_arena/cancel_interval"
	pass
class GrandArenaResetBattleNumberRequest(Request[GrandArenaResetBattleNumberResponse]):
	@property
	def url(self) -> str:
		return "grand_arena/reset_battle_number"
	pass
class GrandArenaRankingRequest(Request[GrandArenaRankingResponse]):
	limit: int = None
	page: int = None
	@property
	def url(self) -> str:
		return "grand_arena/ranking"
class GrandArenaHistoryRequest(Request[GrandArenaHistoryResponse]):
	@property
	def url(self) -> str:
		return "grand_arena/history"
	pass
class GrandArenaHistoryDetailRequest(Request[GrandArenaHistoryDetailResponse]):
	log_id: int = None
	@property
	def url(self) -> str:
		return "grand_arena/history_detail"
class GrandArenaReplayRequest(Request[GrandArenaReplayResponse]):
	log_id: int = None
	round: int = None
	@property
	def url(self) -> str:
		return "grand_arena/replay"
class GrandArenaGetDestinationGroupRequest(Request[GrandArenaGetDestinationGroupResponse]):
	@property
	def url(self) -> str:
		return "grand_arena/get_destination_group"
	pass
class GrandArenaMoveGroupRequest(Request[GrandArenaMoveGroupResponse]):
	group_id: int = None
	@property
	def url(self) -> str:
		return "grand_arena/move_group"
class GrandArenaTimeRewardAcceptRequest(Request[GrandArenaTimeRewardAcceptResponse]):
	@property
	def url(self) -> str:
		return "grand_arena/time_reward_accept"
	pass
class HatsuneTopRequest(Request[HatsuneTopResponse]):
	event_id: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/top"
class HatsuneQuestTopRequest(Request[HatsuneQuestTopResponse]):
	event_id: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/quest_top"
class HatsuneQuestStartRequest(Request[HatsuneQuestStartResponse]):
	event_id: int = None
	quest_id: int = None
	token: str = None
	owner_viewer_id: int = None
	support_unit_id: int = None
	support_battle_rarity: int = None
	is_friend: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/quest_start"
class HatsuneQuestFinishRequest(Request[HatsuneQuestFinishResponse]):
	event_id: int = None
	quest_id: int = None
	remain_time: int = None
	unit_hp_list: List[UnitHpInfo] = None
	owner_viewer_id: int = None
	support_position: int = None
	is_friend: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/quest_finish"
class HatsuneQuestRetireRequest(Request[HatsuneQuestRetireResponse]):
	event_id: int = None
	quest_id: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/quest_retire"
class HatsuneQuestSkipRequest(Request[HatsuneQuestSkipResponse]):
	event_id: int = None
	quest_id: int = None
	use_ticket_num: int = None
	current_ticket_num: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/quest_skip"
class HatsuneMissionIndexRequest(Request[HatsuneMissionIndexResponse]):
	event_id: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/mission_index"
class HatsuneMissionAcceptRequest(Request[HatsuneMissionAcceptResponse]):
	event_id: int = None
	type: int = None
	id: int = None
	buy_id: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/mission_accept"
class HatsuneBossBattleStartRequest(Request[HatsuneBossBattleStartResponse]):
	event_id: int = None
	boss_id: int = None
	current_ticket_num: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/boss_battle_start"
class HatsuneBossBattleFinishRequest(Request[HatsuneBossBattleFinishResponse]):
	event_id: int = None
	boss_id: int = None
	user_unit: HatsuneBossBattleFinishUnit = None
	remain_time: int = None
	total_damage: int = None
	enemy_damage_list: List[EventEnemyDamageInfo] = None
	@property
	def url(self) -> str:
		return "event/hatsune/boss_battle_finish"
class HatsuneBossBattleSkipRequest(Request[HatsuneBossBattleSkipResponse]):
	event_id: int = None
	boss_id: int = None
	exec_skip_num: int = None
	current_skip_ticket_num: int = None
	current_boss_ticket_num: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/boss_battle_skip"
class HatsuneRecoverChallengeRequest(Request[HatsuneRecoverChallengeResponse]):
	quest_id: int = None
	current_currency_num: int = None
	event_id: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/recover_challenge"
class HatsuneSpecialBattleStartRequest(Request[HatsuneSpecialBattleStartResponse]):
	boss_id: int = None
	event_id: int = None
	current_ticket_num: int = None
	mode: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/special_battle_start"
class HatsuneSpecialBattleFinishRequest(Request[HatsuneSpecialBattleFinishResponse]):
	event_id: int = None
	boss_id: int = None
	user_unit: HatsuneBossBattleFinishUnit = None
	total_damage: int = None
	enemy_damage_list: List[EventEnemyDamageInfo] = None
	remain_time: int = None
	mode: int = None
	enemy_info: List[EventEnemyInfo] = None
	@property
	def url(self) -> str:
		return "event/hatsune/special_battle_finish"
class HatsuneSpecialBattleRetireRequest(Request[HatsuneSpecialBattleRetireResponse]):
	event_id: int = None
	boss_id: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/special_battle_retire"
class HatsuneSpecialBattleExStartRequest(Request[HatsuneSpecialBattleExStartResponse]):
	boss_id: int = None
	event_id: int = None
	mode: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/special_battle_ex_start"
class HatsuneSpecialBattleExFinishRequest(Request[HatsuneSpecialBattleExFinishResponse]):
	event_id: int = None
	boss_id: int = None
	user_unit: HatsuneBossBattleFinishUnit = None
	total_damage: int = None
	enemy_damage_list: List[EventEnemyDamageInfo] = None
	remain_time: int = None
	mode: int = None
	enemy_info: List[EventEnemyInfo] = None
	manual_flags: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/special_battle_ex_finish"
class HatsuneSpecialBattleExRetireRequest(Request[HatsuneSpecialBattleExRetireResponse]):
	event_id: int = None
	boss_id: int = None
	manual_flags: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/special_battle_ex_retire"
class HatsuneSpecialBattleExHistoryRequest(Request[HatsuneSpecialBattleExHistoryResponse]):
	event_id: int = None
	appear_num: int = None
	page: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/special_battle_ex_history"
class HatsuneSpecialBattleExResetRequest(Request[HatsuneSpecialBattleExResetResponse]):
	event_id: int = None
	boss_id: int = None
	appear_num: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/special_battle_ex_reset"
class HatsuneQuizAnswerRequest(Request[HatsuneQuizAnswerResponse]):
	event_id: int = None
	quiz_id: int = None
	choice: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/quiz_answer"
class HatsuneDearTopRequest(Request[HatsuneDearTopResponse]):
	event_id: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/dear_top"
class HatsuneDearFinishRequest(Request[HatsuneDearFinishResponse]):
	event_id: int = None
	story_id: int = None
	choice: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/dear_finish"
class HatsuneReadDiaryRequest(Request[HatsuneReadDiaryResponse]):
	diary_id: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/read_diary"
class HatsuneReadRelayStoryRequest(Request[HatsuneReadRelayStoryResponse]):
	relay_story_id: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/read_relay_story"
class HatsuneReadOmpStoryRequest(Request[HatsuneReadOmpStoryResponse]):
	omp_story_id: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/read_omp_story"
class HatsuneReadNyxStoryRequest(Request[HatsuneReadNyxStoryResponse]):
	id: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/read_nyx_story"
class HatsuneChangeNyxItemColorRequest(Request[HatsuneChangeNyxItemColorResponse]):
	color_id: int = None
	@property
	def url(self) -> str:
		return "event/hatsune/change_nyx_item_color"
class HomeIndexRequest(Request[HomeIndexResponse]):
	message_id: int = None
	tips_id_list: List[int] = None
	is_first: int = None
	gold_history: int = None
	@property
	def url(self) -> str:
		return "home/index"
class ItemETicketExchangeRequest(Request[ItemETicketExchangeResponse]):
	ticket_id: int = None
	ticket_count: int = None
	exchange_number: int = None
	@property
	def url(self) -> str:
		return "item_e_ticket/exchange"
class UseExpItemRequest(Request[UseExpItemResponse]):
	item_list: List[ItemInfo] = None
	unit_id: int = None
	@property
	def url(self) -> str:
		return "item/exp"
class SellItemRequest(Request[SellItemResponse]):
	item_type: int = None
	item_id: int = None
	item_num: int = None
	current_item_num: int = None
	@property
	def url(self) -> str:
		return "item/sell"
class MusicBuyRequest(Request[MusicBuyResponse]):
	music_id: int = None
	room_coin: int = None
	@property
	def url(self) -> str:
		return "music/buy"
class MusicTopRequest(Request[MusicTopResponse]):
	@property
	def url(self) -> str:
		return "music/top"
	pass
class MusicSetRequest(Request[MusicSetResponse]):
	bgm: List[MusicIdData] = None
	@property
	def url(self) -> str:
		return "music/set"
class KaiserBattleTopRequest(Request[KaiserBattleTopResponse]):
	@property
	def url(self) -> str:
		return "kaiser_battle/top"
	pass
class KaiserBattleUpdateDeckRequest(Request[KaiserBattleUpdateDeckResponse]):
	kaiser_boss_id: int = None
	unit_id_1: int = None
	unit_id_2: int = None
	unit_id_3: int = None
	unit_id_4: int = None
	unit_id_5: int = None
	@property
	def url(self) -> str:
		return "kaiser_battle/update_deck"
class KaiserBattleSubStartRequest(Request[KaiserBattleSubStartResponse]):
	kaiser_boss_id: int = None
	token: str = None
	support_list: List[KaiserBattleSupportRental] = None
	@property
	def url(self) -> str:
		return "kaiser_battle/sub_start"
class KaiserBattleSubFinishRequest(Request[KaiserBattleSubFinishResponse]):
	kaiser_boss_id: int = None
	battle_log_id: int = None
	remaining_count: int = None
	remain_time: int = None
	total_damage: int = None
	battle_finish_unit: BossBattleFinishUnit = None
	@property
	def url(self) -> str:
		return "kaiser_battle/sub_finish"
class KaiserBattleMainStartRequest(Request[KaiserBattleMainStartResponse]):
	kaiser_boss_id: int = None
	token: str = None
	mode: int = None
	from_event_flag: int = None
	support_list: List[KaiserBattleSupportRental] = None
	@property
	def url(self) -> str:
		return "kaiser_battle/main_start"
class KaiserBattleMainFinishRequest(Request[KaiserBattleMainFinishResponse]):
	kaiser_boss_id: int = None
	battle_log_id: int = None
	remain_time: int = None
	total_damage: int = None
	mode: int = None
	battle_finish_unit: BossBattleFinishUnit = None
	enemy_info: List[EventEnemyInfo] = None
	@property
	def url(self) -> str:
		return "kaiser_battle/main_finish"
class KaiserBattleMainRetireRequest(Request[KaiserBattleMainRetireResponse]):
	kaiser_boss_id: int = None
	battle_log_id: int = None
	@property
	def url(self) -> str:
		return "kaiser_battle/main_retire"
class KaiserBattleSetSupportUnitRequest(Request[KaiserBattleSetSupportUnitResponse]):
	position: int = None
	unit_id: int = None
	@property
	def url(self) -> str:
		return "kaiser_battle/set_support_unit"
class KaiserBattleSupportListRequest(Request[KaiserBattleSupportListResponse]):
	kaiser_boss_id: int = None
	@property
	def url(self) -> str:
		return "kaiser_battle/support_list"
class KaiserBattleGetMainBossInfoRequest(Request[KaiserBattleGetMainBossInfoResponse]):
	@property
	def url(self) -> str:
		return "kaiser_battle/get_main_boss_info"
	pass
class KaiserBattleMySupportListRequest(Request[KaiserBattleMySupportListResponse]):
	@property
	def url(self) -> str:
		return "kaiser_battle/my_support_list"
	pass
class KmkTopRequest(Request[KmkTopResponse]):
	@property
	def url(self) -> str:
		return "kmk/top"
	pass
class KmkStartRequest(Request[KmkStartResponse]):
	difficulty_level: int = None
	@property
	def url(self) -> str:
		return "kmk/start"
class KmkFinishRequest(Request[KmkFinishResponse]):
	play_id: int = None
	base_score: int = None
	kill_list: KmkKillList = None
	max_combo_count: int = None
	after_hp: int = None
	fever_score: int = None
	@property
	def url(self) -> str:
		return "kmk/finish"
class LoadIndexRequest(Request[LoadIndexResponse]):
	carrier: str = None
	@property
	def url(self) -> str:
		return "load/index"
class LoadNextDayIndexRequest(Request[LoadNextDayIndexResponse]):
	carrier: str = None
	@property
	def url(self) -> str:
		return "load/next_day_index"
class RaceLoginBonusCharaSelectDataRequest(Request[RaceLoginBonusCharaSelectDataResponse]):
	fortune_id: int = None
	unit_id: int = None
	battle_log_id: int = None
	frame_rate: int = None
	battle_log: str = None
	system_id: int = None
	@property
	def url(self) -> str:
		return "chara_fortune/draw"
class MissionIndexRequest(Request[MissionIndexResponse]):
	request_flag: MissionRequestFlag = None
	@property
	def url(self) -> str:
		return "mission/index"
class MissionAcceptRequest(Request[MissionAcceptResponse]):
	type: int = None
	id: int = None
	buy_id: int = None
	@property
	def url(self) -> str:
		return "mission/accept"
class MyPageSetMyPageRequest(Request[MyPageSetMyPageResponse]):
	my_page_info: List[MyPage] = None
	@property
	def url(self) -> str:
		return "my_page/set_my_page"
class SetMyPartyRequest(Request[SetMyPartyResponse]):
	tab_number: int = None
	party_number: int = None
	party_label_type: int = None
	party_name: str = None
	unit_id_1: int = None
	unit_id_2: int = None
	unit_id_3: int = None
	unit_id_4: int = None
	unit_id_5: int = None
	change_rarity_unit_list: List[ChangeRarityUnit] = None
	@property
	def url(self) -> str:
		return "my_party/set_party"
class SetMyPartyTabRequest(Request[SetMyPartyTabResponse]):
	tab_number: int = None
	tab_name: str = None
	@property
	def url(self) -> str:
		return "my_party/set_tab"
class UpdateSkipQuestListRequest(Request[UpdateSkipQuestListResponse]):
	my_quest_tab_list: List[UserMyQuestForPost] = None
	@property
	def url(self) -> str:
		return "my_quest/update_skip_quest_list"
class UpdateTabRequest(Request[UpdateTabResponse]):
	tab_number: int = None
	tab_name: str = None
	@property
	def url(self) -> str:
		return "my_quest/update_tab"
class PctTopRequest(Request[PctTopResponse]):
	@property
	def url(self) -> str:
		return "pct/top"
	pass
class PctStartRequest(Request[PctStartResponse]):
	unit_id: int = None
	use_item_id: int = None
	use_item_count: int = None
	@property
	def url(self) -> str:
		return "pct/start"
class PctFinishRequest(Request[PctFinishResponse]):
	pct_play_id: int = None
	base_pct_point: int = None
	max_combo_count: int = None
	grade_list: List[PctGradeInfo] = None
	barrage_count: int = None
	fruits_count: int = None
	special_item_count: int = None
	fever_count: int = None
	@property
	def url(self) -> str:
		return "pct/finish"
class PictureBookRequest(Request[PictureBookResponse]):
	mode: int = None
	@property
	def url(self) -> str:
		return "picture_book/index"
class PkbTopRequest(Request[PkbTopResponse]):
	from_system_id: int = None
	@property
	def url(self) -> str:
		return "pkb/top"
class PkbStartSoloRequest(Request[PkbStartSoloResponse]):
	difficulty_level: int = None
	batter_id: int = None
	from_system_id: int = None
	happen_mode: ePkbHappenMode = None
	@property
	def url(self) -> str:
		return "pkb/start_solo"
class PkbStartVsRequest(Request[PkbStartVsResponse]):
	difficulty_level: int = None
	batter_id: int = None
	vs_batter_id: int = None
	from_system_id: int = None
	happen_mode: ePkbHappenMode = None
	@property
	def url(self) -> str:
		return "pkb/start_vs"
class PkbFinishSoloRequest(Request[PkbFinishSoloResponse]):
	play_id: int = None
	result_type: int = None
	total_batting_distance: int = None
	single_max_batting_distance: int = None
	home_run_num: int = None
	hit_num: int = None
	batting_result_list: List[PkbBattingResultInfo] = None
	ball_type_list: List[int] = None
	elapsed_frame: int = None
	from_system_id: int = None
	happen_mode: ePkbHappenMode = None
	@property
	def url(self) -> str:
		return "pkb/finish_solo"
class PkbFinishVsRequest(Request[PkbFinishVsResponse]):
	play_id: int = None
	result_type: int = None
	base_score: int = None
	vs_base_score: int = None
	total_batting_distance: int = None
	single_max_batting_distance: int = None
	home_run_num: int = None
	hit_num: int = None
	batting_result_list: List[PkbBattingResultInfo] = None
	ball_type_list: List[int] = None
	elapsed_frame: int = None
	from_system_id: int = None
	happen_mode: ePkbHappenMode = None
	@property
	def url(self) -> str:
		return "pkb/finish_vs"
class PkbReadCatalogRequest(Request[PkbReadCatalogResponse]):
	pitcher_id_list: List[int] = None
	batter_id_list: List[int] = None
	from_system_id: int = None
	@property
	def url(self) -> str:
		return "pkb/read_catalog"
class PkbReadRankingRequest(Request[PkbReadRankingResponse]):
	read_ranking_info: List[PkbReadRankingInfo] = None
	read_simple_ranking_info: List[PkbReadRankingInfo] = None
	from_system_id: int = None
	@property
	def url(self) -> str:
		return "pkb/read_ranking"
class FriendBattleTopRequest(Request[FriendBattleTopResponse]):
	is_clan: int = None
	@property
	def url(self) -> str:
		return "practice/friend_battle_top"
class FriendBattleUpdateDeckRequest(Request[FriendBattleUpdateDeckResponse]):
	deck_number: int = None
	deck_name: str = None
	unit_id_1: int = None
	unit_id_2: int = None
	unit_id_3: int = None
	unit_id_4: int = None
	unit_id_5: int = None
	mask_bit_flag: int = None
	@property
	def url(self) -> str:
		return "practice/update_deck"
class FriendBattleStartRequest(Request[FriendBattleStartResponse]):
	battle_viewer_id: int = None
	deck_number: int = None
	disable_skin: int = None
	is_clan: int = None
	@property
	def url(self) -> str:
		return "practice/friend_battle_start"
class FriendBattleFinishRequest(Request[FriendBattleFinishResponse]):
	battle_id: int = None
	wave_result_list: List[FriendBattleResult] = None
	@property
	def url(self) -> str:
		return "practice/friend_battle_finish"
class PresentIndexRequest(Request[PresentIndexResponse]):
	time_filter: int = None
	type_filter: int = None
	desc_flag: bool = None
	offset: int = None
	@property
	def url(self) -> str:
		return "present/index"
class PresentReceiveSingleRequest(Request[PresentReceiveSingleResponse]):
	present_id: int = None
	@property
	def url(self) -> str:
		return "present/receive"
class PresentReceiveAllRequest(Request[PresentReceiveAllResponse]):
	time_filter: int = None
	type_filter: int = None
	desc_flag: bool = None
	is_exclude_stamina: bool = None
	@property
	def url(self) -> str:
		return "present/receive_all"
class PresentHistoryRequest(Request[PresentHistoryResponse]):
	page: int = None
	@property
	def url(self) -> str:
		return "present/history"
class ProfileGetRequest(Request[ProfileGetResponse]):
	target_viewer_id: int = None
	@property
	def url(self) -> str:
		return "profile/get_profile"
class ProfileRenameRequest(Request[ProfileRenameResponse]):
	user_name: str = None
	@property
	def url(self) -> str:
		return "profile/rename"
class ProfileUpdateCommentRequest(Request[ProfileUpdateCommentResponse]):
	user_comment: str = None
	@property
	def url(self) -> str:
		return "profile/update_comment"
class ProfileFavoriteUnitRequest(Request[ProfileFavoriteUnitResponse]):
	unit_id: int = None
	@property
	def url(self) -> str:
		return "profile/favorite_unit"
class ProfileSetBirthDayRequest(Request[ProfileSetBirthDayResponse]):
	birthday: int = None
	@property
	def url(self) -> str:
		return "profile/set_birthday"
class ProfileMakerGetMyProfileRequest(Request[ProfileMakerGetMyProfileResponse]):
	@property
	def url(self) -> str:
		return "profile_maker/get_my_profile"
	pass
class ProfileMakerSetMyProfileRequest(Request[ProfileMakerSetMyProfileResponse]):
	profile: MyProfileCardSetting = None
	@property
	def url(self) -> str:
		return "profile_maker/set_my_profile"
class ProfileMakerGetClanProfileRequest(Request[ProfileMakerGetClanProfileResponse]):
	@property
	def url(self) -> str:
		return "profile_maker/get_clan_profile"
	pass
class ProfileMakerSetClanProfileRequest(Request[ProfileMakerSetClanProfileResponse]):
	profile: ClanProfileCardSetting = None
	@property
	def url(self) -> str:
		return "profile_maker/set_clan_profile"
class QuestStartRequest(Request[QuestStartResponse]):
	quest_id: int = None
	token: str = None
	owner_viewer_id: int = None
	support_unit_id: int = None
	support_battle_rarity: int = None
	is_friend: int = None
	@property
	def url(self) -> str:
		return "quest/start"
class QuestFinishRequest(Request[QuestFinishResponse]):
	quest_id: int = None
	remain_time: int = None
	unit_hp_list: List[UnitHpInfo] = None
	auto_clear: int = None
	fps: int = None
	owner_viewer_id: int = None
	support_position: int = None
	is_friend: int = None
	@property
	def url(self) -> str:
		return "quest/finish"
class QuestRetireRequest(Request[QuestRetireResponse]):
	quest_id: int = None
	@property
	def url(self) -> str:
		return "quest/retire"
class QuestSkipRequest(Request[QuestSkipResponse]):
	quest_id: int = None
	random_count: int = None
	current_ticket_num: int = None
	@property
	def url(self) -> str:
		return "quest/quest_skip"
class QuestSkipMultipleRequest(Request[QuestSkipMultipleResponse]):
	normal_skip_list: List[QuestSkipInfo] = None
	hard_skip_list: List[QuestSkipInfo] = None
	very_hard_skip_list: List[QuestSkipInfo] = None
	shiori_hard_skip_list: List[QuestSkipInfo] = None
	current_ticket_num: int = None
	@property
	def url(self) -> str:
		return "quest/quest_skip_multiple"
class QuestRecoverChallengeRequest(Request[QuestRecoverChallengeResponse]):
	quest_id: int = None
	current_currency_num: int = None
	@property
	def url(self) -> str:
		return "quest/recover_challenge"
class QuestRecoverChallengeMultipleRequest(Request[QuestRecoverChallengeMultipleResponse]):
	hard_quest_list: List[int] = None
	very_hard_quest_list: List[int] = None
	current_currency_num: int = None
	@property
	def url(self) -> str:
		return "quest/recover_challenge_multiple"
class TrainingQuestStartRequest(Request[TrainingQuestStartResponse]):
	quest_id: int = None
	token: str = None
	owner_viewer_id: int = None
	support_unit_id: int = None
	support_battle_rarity: int = None
	is_friend: int = None
	@property
	def url(self) -> str:
		return "training_quest/start"
class TrainingQuestFinishRequest(Request[TrainingQuestFinishResponse]):
	quest_id: int = None
	remain_time: int = None
	unit_hp_list: List[UnitHpInfo] = None
	owner_viewer_id: int = None
	support_position: int = None
	is_friend: int = None
	@property
	def url(self) -> str:
		return "training_quest/finish"
class TrainingQuestRetireRequest(Request[TrainingQuestRetireResponse]):
	quest_id: int = None
	@property
	def url(self) -> str:
		return "training_quest/retire"
class TrainingQuestSkipRequest(Request[TrainingQuestSkipResponse]):
	quest_id: int = None
	random_count: int = None
	current_ticket_num: int = None
	@property
	def url(self) -> str:
		return "training_quest/quest_skip"
class QuestReplayListRequest(Request[QuestReplayListResponse]):
	quest_id: int = None
	fps: int = None
	team_level: int = None
	@property
	def url(self) -> str:
		return "quest/replay_list"
class QuestReplayRequest(Request[QuestReplayResponse]):
	quest_id: int = None
	enc_key: str = None
	@property
	def url(self) -> str:
		return "quest/replay"
class QuestReplayReportRequest(Request[QuestReplayReportResponse]):
	enc_key: str = None
	quest_id: int = None
	@property
	def url(self) -> str:
		return "quest/replay_report"
class RaritySixQuestStartRequest(Request[RaritySixQuestStartResponse]):
	quest_id: int = None
	token: str = None
	@property
	def url(self) -> str:
		return "rarity_6_quest/start"
class RaritySixQuestFinishRequest(Request[RaritySixQuestFinishResponse]):
	quest_id: int = None
	remain_time: int = None
	unit_hp_list: List[UnitHpInfo] = None
	@property
	def url(self) -> str:
		return "rarity_6_quest/finish"
class RoomStartRequest(Request[RoomStartResponse]):
	wac_auto_option_flag: int = None
	@property
	def url(self) -> str:
		return "room/start"
class RoomUpdateRequest(Request[RoomUpdateResponse]):
	floor_number: int = None
	layout: RoomFloorLayout = None
	background_theme: int = None
	@property
	def url(self) -> str:
		return "room/update"
class RoomVisitRequest(Request[RoomVisitResponse]):
	target_viewer_id: int = None
	@property
	def url(self) -> str:
		return "room/visit"
class RoomLikeRequest(Request[RoomLikeResponse]):
	target_viewer_id: int = None
	@property
	def url(self) -> str:
		return "room/like"
class RoomLikeHistoryRequest(Request[RoomLikeHistoryResponse]):
	@property
	def url(self) -> str:
		return "room/like_history"
	pass
class RoomClanMemberRequest(Request[RoomClanMemberResponse]):
	@property
	def url(self) -> str:
		return "room/clan_member"
class RoomExtendStorageRequest(Request[RoomExtendStorageResponse]):
	storage_num: int = None
	@property
	def url(self) -> str:
		return "room/extend_storage"
class RoomItemBuyRequest(Request[RoomItemBuyResponse]):
	item_id: int = None
	item_count: int = None
	purchase_type: int = None
	floor_number: int = None
	background_theme: int = None
	layout: RoomFloorLayout = None
	has_update: int = None
	room_coin: int = None
	@property
	def url(self) -> str:
		return "room/buy"
class RoomItemSellRequest(Request[RoomItemSellResponse]):
	serial_id_list: List[int] = None
	floor_number: int = None
	background_theme: int = None
	layout: RoomFloorLayout = None
	@property
	def url(self) -> str:
		return "room/sell"
class RoomGiveGiftRequest(Request[RoomGiveGiftResponse]):
	unit_id: int = None
	item_id: int = None
	item_num: int = None
	current_item_num: int = None
	@property
	def url(self) -> str:
		return "room/give_gift"
class RoomLevelUpStartRequest(Request[RoomLevelUpStartResponse]):
	floor_number: int = None
	serial_id: int = None
	@property
	def url(self) -> str:
		return "room/level_up_start"
class RoomLevelUpStopRequest(Request[RoomLevelUpStopResponse]):
	serial_id: int = None
	@property
	def url(self) -> str:
		return "room/level_up_stop"
class RoomLevelUpEndRequest(Request[RoomLevelUpEndResponse]):
	serial_id: int = None
	@property
	def url(self) -> str:
		return "room/level_up_end"
class RoomMultiGiveGiftRequest(Request[RoomMultiGiveGiftResponse]):
	unit_id: int = None
	item_info: List[SendGiftData] = None
	@property
	def url(self) -> str:
		return "room/multi_give_gift"
class RoomMultiLevelUpEndRequest(Request[RoomMultiLevelUpEndResponse]):
	serial_id_list: List[int] = None
	@property
	def url(self) -> str:
		return "room/multi_level_up_end"
class RoomLevelUpShorteningRequest(Request[RoomLevelUpShorteningResponse]):
	serial_id: int = None
	@property
	def url(self) -> str:
		return "room/level_up_shortening"
class RoomReceiveItemRequest(Request[RoomReceiveItemResponse]):
	serial_id: int = None
	@property
	def url(self) -> str:
		return "room/receive"
class RoomReceiveItemAllRequest(Request[RoomReceiveItemAllResponse]):
	@property
	def url(self) -> str:
		return "room/receive_all"
class RoomMysetListRequest(Request[RoomMysetListResponse]):
	@property
	def url(self) -> str:
		return "room/myset_list"
class RoomMysetSaveRequest(Request[RoomMysetSaveResponse]):
	myset_index: int = None
	background_theme: int = None
	floor_layout: RoomFloorLayoutForMyset = None
	@property
	def url(self) -> str:
		return "room/save_myset"
class RoomMysetDeleteRequest(Request[RoomMysetDeleteResponse]):
	myset_index: int = None
	@property
	def url(self) -> str:
		return "room/delete_myset"
class RoomMysetRenameRequest(Request[RoomMysetRenameResponse]):
	myset_index: int = None
	new_name: str = None
	@property
	def url(self) -> str:
		return "room/rename_myset"
class RoomFreeGiftRequest(Request[RoomFreeGiftResponse]):
	unit_id: int = None
	after_love_level: int = None
	@property
	def url(self) -> str:
		return "room/free_gift"
class SekaiBossInfoRequest(Request[SekaiBossInfoResponse]):
	sekai_id: int = None
	@property
	def url(self) -> str:
		return "sekai/boss_info"
class SekaiTopRequest(Request[SekaiTopResponse]):
	@property
	def url(self) -> str:
		return "sekai/top"
	pass
class SekaiStartRequest(Request[SekaiStartResponse]):
	sekai_id: int = None
	owner_viewer_id: int = None
	support_unit_id: int = None
	token: str = None
	@property
	def url(self) -> str:
		return "sekai/start"
class SekaiFinishRequest(Request[SekaiFinishResponse]):
	sekai_id: int = None
	user_unit: BossBattleFinishUnit = None
	boss_hp: int = None
	boss_damage: int = None
	remain_time: int = None
	total_damage: int = None
	score: int = None
	battle_log_id: int = None
	@property
	def url(self) -> str:
		return "sekai/finish"
class SekaiHistoryReportRequest(Request[SekaiHistoryReportResponse]):
	sekai_id: int = None
	history_id: int = None
	history_viewer_id: int = None
	@property
	def url(self) -> str:
		return "sekai/history_report"
class SekaiRankingRequest(Request[SekaiRankingResponse]):
	sekai_id: int = None
	page: int = None
	is_mine: int = None
	@property
	def url(self) -> str:
		return "sekai/ranking"
class SekaiRankingInClanRequest(Request[SekaiRankingInClanResponse]):
	clan_id: int = None
	sekai_id: int = None
	@property
	def url(self) -> str:
		return "sekai/ranking_in_clan"
class SekaiRetireRequest(Request[SekaiRetireResponse]):
	clan_id: int = None
	sekai_id: int = None
	@property
	def url(self) -> str:
		return "sekai/retire"
class SekaiSupportUnitList2Request(Request[SekaiSupportUnitList2Response]):
	clan_id: int = None
	@property
	def url(self) -> str:
		return "sekai/support_unit_list_2"
class SerialCodeRegisterRequest(Request[SerialCodeRegisterResponse]):
	serial_code: str = None
	@property
	def url(self) -> str:
		return "serial_code/register"
class ShioriTopRequest(Request[ShioriTopResponse]):
	@property
	def url(self) -> str:
		return "shiori/top"
class ShioriFavoriteRequest(Request[ShioriFavoriteResponse]):
	event_id: int = None
	favorite_flag: int = None
	@property
	def url(self) -> str:
		return "event/shiori/favorite"
class ShioriEventTopRequest(Request[ShioriEventTopResponse]):
	event_id: int = None
	@property
	def url(self) -> str:
		return "event/shiori/event_top"
class ShioriQuestStartRequest(Request[ShioriQuestStartResponse]):
	event_id: int = None
	quest_id: int = None
	token: str = None
	owner_viewer_id: int = None
	support_unit_id: int = None
	support_battle_rarity: int = None
	is_friend: int = None
	@property
	def url(self) -> str:
		return "event/shiori/quest_start"
class ShioriQuestFinishRequest(Request[ShioriQuestFinishResponse]):
	event_id: int = None
	quest_id: int = None
	remain_time: int = None
	unit_hp_list: List[UnitHpInfo] = None
	owner_viewer_id: int = None
	support_position: int = None
	is_friend: int = None
	battle_log_id: int = None
	@property
	def url(self) -> str:
		return "event/shiori/quest_finish"
class ShioriQuestRetireRequest(Request[ShioriQuestRetireResponse]):
	event_id: int = None
	quest_id: int = None
	battle_log_id: int = None
	@property
	def url(self) -> str:
		return "event/shiori/quest_retire"
class ShioriQuestSkipRequest(Request[ShioriQuestSkipResponse]):
	event_id: int = None
	quest_id: int = None
	use_ticket_num: int = None
	current_ticket_num: int = None
	@property
	def url(self) -> str:
		return "event/shiori/quest_skip"
class ShioriMissionIndexRequest(Request[ShioriMissionIndexResponse]):
	event_id: int = None
	@property
	def url(self) -> str:
		return "event/shiori/mission_index"
class ShioriMissionAcceptRequest(Request[ShioriMissionAcceptResponse]):
	event_id: int = None
	type: int = None
	id: int = None
	buy_id: int = None
	@property
	def url(self) -> str:
		return "event/shiori/mission_accept"
class ShioriBossBattleStartRequest(Request[ShioriBossBattleStartResponse]):
	event_id: int = None
	boss_id: int = None
	token: str = None
	@property
	def url(self) -> str:
		return "event/shiori/boss_battle_start"
class ShioriBossBattleFinishRequest(Request[ShioriBossBattleFinishResponse]):
	event_id: int = None
	boss_id: int = None
	user_unit: HatsuneBossBattleFinishUnit = None
	remain_time: int = None
	total_damage: int = None
	battle_log_id: int = None
	@property
	def url(self) -> str:
		return "event/shiori/boss_battle_finish"
class ShioriBossBattleRetireRequest(Request[ShioriBossBattleRetireResponse]):
	event_id: int = None
	boss_id: int = None
	battle_log_id: int = None
	@property
	def url(self) -> str:
		return "event/shiori/boss_battle_retire"
class ShioriQuizAnswerRequest(Request[ShioriQuizAnswerResponse]):
	event_id: int = None
	quiz_id: int = None
	choice: int = None
	@property
	def url(self) -> str:
		return "event/shiori/quiz_answer"
class ShioriDearTopRequest(Request[ShioriDearTopResponse]):
	event_id: int = None
	@property
	def url(self) -> str:
		return "event/shiori/dear_top"
class ShioriDearFinishRequest(Request[ShioriDearFinishResponse]):
	event_id: int = None
	story_id: int = None
	choice: int = None
	@property
	def url(self) -> str:
		return "event/shiori/dear_finish"
class ShopItemListRequest(Request[ShopItemListResponse]):
	@property
	def url(self) -> str:
		return "shop/item_list"
	pass
class ShopBuyRequest(Request[ShopBuyResponse]):
	system_id: int = None
	slot_id: int = None
	current_currency_num: int = None
	number: int = None
	total_price: int = None
	@property
	def url(self) -> str:
		return "shop/buy"
class ShopBuyMultipleRequest(Request[ShopBuyMultipleResponse]):
	system_id: int = None
	slot_ids: List[int] = None
	current_currency_num: int = None
	@property
	def url(self) -> str:
		return "shop/buy_multiple"
class ShopResetRequest(Request[ShopResetResponse]):
	system_id: int = None
	current_currency_num: int = None
	@property
	def url(self) -> str:
		return "shop/reset"
class ShopAlchemyRequest(Request[ShopAlchemyResponse]):
	multiple_count: int = None
	pay_or_free: int = None
	current_currency_num: int = None
	@property
	def url(self) -> str:
		return "shop/alchemy"
class ShopRecoverStaminaRequest(Request[ShopRecoverStaminaResponse]):
	current_currency_num: int = None
	@property
	def url(self) -> str:
		return "shop/recover_stamina"
class ShopCloseLimitedShopRequest(Request[ShopCloseLimitedShopResponse]):
	system_id: int = None
	appear_count: int = None
	close_time: int = None
	@property
	def url(self) -> str:
		return "shop/close_limited_shop"
class ShopCloseDailyShopRequest(Request[ShopCloseDailyShopResponse]):
	system_id: int = None
	@property
	def url(self) -> str:
		return "shop/close_daily_shop"
class ShopComebackTutorialDailyShopRequest(Request[ShopComebackTutorialDailyShopResponse]):
	@property
	def url(self) -> str:
		return "shop/comeback_tutorial_daily_shop"
	pass
class SkillSetFreeRequest(Request[SkillSetFreeResponse]):
	unit_id: int = None
	location: int = None
	origin_unit_id: int = None
	origin_location: int = None
	@property
	def url(self) -> str:
		return "skill/set_free"
class SkillRemoveFreeRequest(Request[SkillRemoveFreeResponse]):
	unit_id: int = None
	location: int = None
	@property
	def url(self) -> str:
		return "skill/remove_free"
class SkillLevelUpRequest(Request[SkillLevelUpResponse]):
	unit_id: int = None
	skill_levelup_list: List[SkillLevelUpDetail] = None
	@property
	def url(self) -> str:
		return "skill/level_up"
class SpaceTopRequest(Request[SpaceTopResponse]):
	@property
	def url(self) -> str:
		return "space/top"
	pass
class SpaceStartRequest(Request[SpaceStartResponse]):
	space_id: int = None
	space_battle_id: int = None
	owner_viewer_id: int = None
	support_unit_id: int = None
	token: str = None
	@property
	def url(self) -> str:
		return "space/start"
class SpaceFinishRequest(Request[SpaceFinishResponse]):
	space_id: int = None
	space_battle_id: int = None
	user_unit: BossBattleFinishUnit = None
	total_damage: int = None
	remain_time: int = None
	battle_log_id: int = None
	@property
	def url(self) -> str:
		return "space/finish"
class SpaceRetireRequest(Request[SpaceRetireResponse]):
	space_id: int = None
	space_battle_id: int = None
	battle_log_id: int = None
	@property
	def url(self) -> str:
		return "space/retire"
class SpaceSupportUnitList2Request(Request[SpaceSupportUnitList2Response]):
	clan_id: int = None
	@property
	def url(self) -> str:
		return "space/support_unit_list_2"
class SpaceStoryCheckRequest(Request[SpaceStoryCheckResponse]):
	story_id: int = None
	@property
	def url(self) -> str:
		return "space/story_check"
class SpaceStoryStartRequest(Request[SpaceStoryStartResponse]):
	story_id: int = None
	space_id: int = None
	progress: int = None
	@property
	def url(self) -> str:
		return "space/story_start"
class SrtTopRequest(Request[SrtTopResponse]):
	@property
	def url(self) -> str:
		return "srt/top"
	pass
class SrtStartRequest(Request[SrtStartResponse]):
	difficulty_level: int = None
	priconne_mode: int = None
	@property
	def url(self) -> str:
		return "srt/start"
class SrtFinishRequest(Request[SrtFinishResponse]):
	play_id: int = None
	result_type: int = None
	base_score: int = None
	turn_num: int = None
	avg_answer_time: int = None
	wrong_num: int = None
	update_catalog_info: List[SrtCatalogInfo] = None
	@property
	def url(self) -> str:
		return "srt/finish"
class SrtReadCatalogRequest(Request[SrtReadCatalogResponse]):
	@property
	def url(self) -> str:
		return "srt/read_catalog"
	pass
class StoryViewingRequest(Request[StoryViewingResponse]):
	story_id: int = None
	@property
	def url(self) -> str:
		return "story/start"
class StoryQuestStartRequest(Request[StoryQuestStartResponse]):
	quest_id: int = None
	@property
	def url(self) -> str:
		return "story/quest_start"
class StoryMaintenanceCheckRequest(Request[StoryMaintenanceCheckResponse]):
	story_id: int = None
	@property
	def url(self) -> str:
		return "story/check"
class StoryForceReleaseRequest(Request[StoryForceReleaseResponse]):
	story_group_id: int = None
	@property
	def url(self) -> str:
		return "story/force_release"
class SubStoryLtoReadStoryRequest(Request[SubStoryLtoReadStoryResponse]):
	sub_story_id: int = None
	@property
	def url(self) -> str:
		return "sub_story/lto/read_story"
class SubStorySkeConfirmRequest(Request[SubStorySkeConfirmResponse]):
	@property
	def url(self) -> str:
		return "sub_story/ske/confirm"
	pass
class SubStorySkeReadStoryRequest(Request[SubStorySkeReadStoryResponse]):
	sub_story_id: int = None
	@property
	def url(self) -> str:
		return "sub_story/ske/read_story"
class SubStorySspReadSspStoryRequest(Request[SubStorySspReadSspStoryResponse]):
	sub_story_id: int = None
	@property
	def url(self) -> str:
		return "sub_story/ssp/read_ssp_story"
class SupportUnitChangeSettingRequest(Request[SupportUnitChangeSettingResponse]):
	support_type: int = None
	position: int = None
	action: int = None
	unit_id: int = None
	@property
	def url(self) -> str:
		return "support_unit/change_setting"
class SupportUnitGetSettingRequest(Request[SupportUnitGetSettingResponse]):
	@property
	def url(self) -> str:
		return "support_unit/get_setting"
	pass
class GetFriendSupportUnitListRequest(Request[GetFriendSupportUnitListResponse]):
	@property
	def url(self) -> str:
		return "SupportUnitGetFriendSupportUnitList"
	pass
class GetTipsListRequest(Request[GetTipsListResponse]):
	@property
	def url(self) -> str:
		return "TipsGetTipsList"
	pass
class AddUserTipsRequest(Request[AddUserTipsResponse]):
	tips_id_list: List[int] = None
	is_first: int = None
	return_cleared_ex_quest: int = None
	@property
	def url(self) -> str:
		return "tips/add_user_tips"
class TowerTopRequest(Request[TowerTopResponse]):
	is_first: int = None
	return_cleared_ex_quest: int = None
	@property
	def url(self) -> str:
		return "tower/top"
class TowerBattleStartRequest(Request[TowerBattleStartResponse]):
	quest_id: int = None
	token: str = None
	owner_viewer_id: int = None
	support_unit_id: int = None
	support_battle_rarity: int = None
	@property
	def url(self) -> str:
		return "tower/battle_start"
class TowerBattleFinishRequest(Request[TowerBattleFinishResponse]):
	quest_id: int = None
	user_unit: List[TowerQueryUnit] = None
	versus_user_unit: List[TowerQueryUnit] = None
	remain_time: int = None
	fps: int = None
	auto_clear: int = None
	@property
	def url(self) -> str:
		return "tower/battle_finish"
class TowerRehearsalStartRequest(Request[TowerRehearsalStartResponse]):
	quest_id: int = None
	token: str = None
	owner_viewer_id: int = None
	support_unit_id: int = None
	support_battle_rarity: int = None
	@property
	def url(self) -> str:
		return "tower/rehearsal_start"
class TowerRehearsalFinishRequest(Request[TowerRehearsalFinishResponse]):
	quest_id: int = None
	user_unit: List[TowerQueryUnit] = None
	versus_user_unit: List[TowerQueryUnit] = None
	remain_time: int = None
	fps: int = None
	auto_clear: int = None
	@property
	def url(self) -> str:
		return "tower/rehearsal_finish"
class TowerSupportUnitListRequest(Request[TowerSupportUnitListResponse]):
	@property
	def url(self) -> str:
		return "tower/support_unit_list"
	pass
class TowerSupportUnitList2Request(Request[TowerSupportUnitList2Response]):
	@property
	def url(self) -> str:
		return "tower/support_unit_list_2"
	pass
class TowerBattleRetireRequest(Request[TowerBattleRetireResponse]):
	quest_id: int = None
	@property
	def url(self) -> str:
		return "tower/battle_retire"
class TowerRehearsalRetireRequest(Request[TowerRehearsalRetireResponse]):
	quest_id: int = None
	@property
	def url(self) -> str:
		return "tower/rehearsal_retire"
class TowerResetRequest(Request[TowerResetResponse]):
	@property
	def url(self) -> str:
		return "tower/reset"
	pass
class TowerExBattleStartRequest(Request[TowerExBattleStartResponse]):
	quest_id: int = None
	token: str = None
	owner_viewer_id: int = None
	support_unit_id: int = None
	support_battle_rarity: int = None
	@property
	def url(self) -> str:
		return "tower/ex_battle_start"
class TowerExBattleFinishRequest(Request[TowerExBattleFinishResponse]):
	quest_id: int = None
	total_damage: int = None
	wave_result_list: List[TowerWaveResultInfo] = None
	versus_user_unit: List[TowerQueryUnit] = None
	fps: int = None
	auto_clear: int = None
	@property
	def url(self) -> str:
		return "tower/ex_battle_finish"
class TowerExSupportUnitListRequest(Request[TowerExSupportUnitListResponse]):
	@property
	def url(self) -> str:
		return "tower/ex_support_unit_list"
	pass
class TowerExSupportUnitList2Request(Request[TowerExSupportUnitList2Response]):
	@property
	def url(self) -> str:
		return "tower/ex_support_unit_list_2"
	pass
class TowerExBattleRetireRequest(Request[TowerExBattleRetireResponse]):
	quest_id: int = None
	@property
	def url(self) -> str:
		return "tower/ex_battle_retire"
class TowerReplayListRequest(Request[TowerReplayListResponse]):
	quest_id: int = None
	fps: int = None
	team_level: int = None
	@property
	def url(self) -> str:
		return "tower/replay_list"
class TowerReplayRequest(Request[TowerReplayResponse]):
	quest_id: int = None
	fps: int = None
	enc_key: str = None
	@property
	def url(self) -> str:
		return "tower/replay"
class TowerReplayReportRequest(Request[TowerReplayReportResponse]):
	quest_id: int = None
	fps: int = None
	enc_key: str = None
	@property
	def url(self) -> str:
		return "tower/replay_report"
class CloisterBattleSkipRequest(Request[CloisterBattleSkipResponse]):
	quest_id: int = None
	skip_count: int = None
	current_ticket_num: int = None
	@property
	def url(self) -> str:
		return "tower/cloister_battle_skip"
class TowerCloisterBattleStartRequest(Request[TowerCloisterBattleStartResponse]):
	quest_id: int = None
	wave: int = None
	token: str = None
	owner_viewer_id: int = None
	support_unit_id: int = None
	support_battle_rarity: int = None
	@property
	def url(self) -> str:
		return "tower/cloister_battle_start"
class TowerCloisterBattleFinishRequest(Request[TowerCloisterBattleFinishResponse]):
	quest_id: int = None
	wave: int = None
	user_unit: List[TowerQueryUnit] = None
	versus_user_unit: List[TowerQueryUnit] = None
	remain_time: int = None
	fps: int = None
	auto_clear: int = None
	@property
	def url(self) -> str:
		return "tower/cloister_battle_finish"
class TowerCloisterBattleRetireRequest(Request[TowerCloisterBattleRetireResponse]):
	quest_id: int = None
	@property
	def url(self) -> str:
		return "tower/cloister_battle_retire"
class TowerBattleSkipRequest(Request[TowerBattleSkipResponse]):
	@property
	def url(self) -> str:
		return "tower/battle_skip"
	pass
class TtkTopRequest(Request[TtkTopResponse]):
	@property
	def url(self) -> str:
		return "ttk/top"
	pass
class TtkChooseWeaponRequest(Request[TtkChooseWeaponResponse]):
	weapon_id: int = None
	@property
	def url(self) -> str:
		return "ttk/choose_weapon"
class TtkReadCatalogRequest(Request[TtkReadCatalogResponse]):
	@property
	def url(self) -> str:
		return "ttk/read_catalog"
	pass
class TtkReadStoryRequest(Request[TtkReadStoryResponse]):
	ttk_story_id: int = None
	@property
	def url(self) -> str:
		return "ttk/read_story"
class TtkStartRequest(Request[TtkStartResponse]):
	difficulty_level: int = None
	@property
	def url(self) -> str:
		return "ttk/start"
class TtkFinishRequest(Request[TtkFinishResponse]):
	play_id: int = None
	base_score: int = None
	coin_num: int = None
	beat_enemy_info: List[TtkBeatEnemyInfo] = None
	remain_life: int = None
	elapsed_frame: int = None
	@property
	def url(self) -> str:
		return "ttk/finish"
class TutorialUpdateRequest(Request[TutorialUpdateResponse]):
	step: int = None
	skip: int = None
	user_name: str = None
	@property
	def url(self) -> str:
		return "tutorial/update_step"
class UekTopRequest(Request[UekTopResponse]):
	event_id: int = None
	@property
	def url(self) -> str:
		return "uek/uek_top"
class UekBossBattleStartRequest(Request[UekBossBattleStartResponse]):
	enemy_id: int = None
	@property
	def url(self) -> str:
		return "uek/boss_battle_start"
class UekBossBattleFinishRequest(Request[UekBossBattleFinishResponse]):
	enemy_id: int = None
	battle_log_id: int = None
	user_unit: HatsuneBossBattleFinishUnit = None
	remain_time: int = None
	total_damage: int = None
	@property
	def url(self) -> str:
		return "uek/boss_battle_finish"
class UekBossBattleRetireRequest(Request[UekBossBattleRetireResponse]):
	enemy_id: int = None
	battle_log_id: int = None
	@property
	def url(self) -> str:
		return "uek/boss_battle_retire"
class AutomaticEnhanceRequest(Request[AutomaticEnhanceResponse]):
	unit_id: int = None
	item_list: List[ItemInfo] = None
	equip_recipe_list: List[UserEquipParameterIdCount] = None
	equip_slot_num_list: List[int] = None
	skill_levelup_list: List[SkillLevelUpDetail] = None
	excludes_equip: int = None
	@property
	def url(self) -> str:
		return "unit/automatic_enhance"
class ChangeSkinRequest(Request[ChangeSkinResponse]):
	skin_data_for_request: SkinDataForRequest = None
	@property
	def url(self) -> str:
		return "unit/change_skin"
class UnlockUnitRequest(Request[UnlockUnitResponse]):
	unit_id: int = None
	@property
	def url(self) -> str:
		return "unit/unlock_unit"
class UnitEquipRequest(Request[UnitEquipResponse]):
	unit_id: int = None
	equip_slot_num: int = None
	@property
	def url(self) -> str:
		return "unit/equip"
class UnitMultiEquipRequest(Request[UnitMultiEquipResponse]):
	unit_id: int = None
	equip_slot_num_list: List[int] = None
	equip_recipe_list: List[UserEquipParameterIdCount] = None
	item_list: List[ItemInfo] = None
	@property
	def url(self) -> str:
		return "unit/multi_equip"
class UnitMultiPromotionRequest(Request[UnitMultiPromotionResponse]):
	target_promotion_level: int = None
	equip_recipe_list: List[RequiredMaterialList] = None
	item_list: List[ItemInfo] = None
	unit_id: int = None
	@property
	def url(self) -> str:
		return "unit/multi_promotion"
class UnitUniqueEquipRequest(Request[UnitUniqueEquipResponse]):
	unit_id: int = None
	equip_slot_num: int = None
	@property
	def url(self) -> str:
		return "unit/equip_unique"
class UnitPromotionRequest(Request[UnitPromotionResponse]):
	unit_id: int = None
	current_promotion_level: int = None
	@property
	def url(self) -> str:
		return "unit/promotion"
class UnitCraftEquipRequest(Request[UnitCraftEquipResponse]):
	unit_id: int = None
	equip_slot_num: int = None
	equip_recipe_list: List[UserEquipParameterIdCount] = None
	item_list: List[ItemInfo] = None
	@property
	def url(self) -> str:
		return "unit/craft_equip"
class UnitCraftEquipUniqueRequest(Request[UnitCraftEquipUniqueResponse]):
	unit_id: int = None
	equip_slot_num: int = None
	equip_recipe_list: List[UserEquipParameterIdCount] = None
	item_recipe_list: List[UserEquipParameterIdCount] = None
	@property
	def url(self) -> str:
		return "unit/craft_equip_unique"
class UnitEvolutionRequest(Request[UnitEvolutionResponse]):
	unit_id: int = None
	current_unit_rarity: int = None
	@property
	def url(self) -> str:
		return "unit/evolution"
class UnitMultiEvolutionRequest(Request[UnitMultiEvolutionResponse]):
	unit_id: int = None
	current_rarity: int = None
	after_rarity: int = None
	current_gold_num: int = None
	current_memory_piece_num: int = None
	@property
	def url(self) -> str:
		return "unit/multi_evolution"
class UnitFavoriteRequest(Request[UnitFavoriteResponse]):
	unit_id_list: List[int] = None
	favorite_flag_list: List[int] = None
	@property
	def url(self) -> str:
		return "unit/favorite"
class UnitEvolutionRaritySixRequest(Request[UnitEvolutionRaritySixResponse]):
	unit_id: int = None
	current_unit_rarity: int = None
	@property
	def url(self) -> str:
		return "unit/evolution_rarity_6"
class UnlockRaritySixSlotRequest(Request[UnlockRaritySixSlotResponse]):
	unit_id: int = None
	slot_id: int = None
	current_unlock_level: int = None
	@property
	def url(self) -> str:
		return "unit/unlock_rarity_6_slot"
class MultiUnlockRaritySixSlotRequest(Request[MultiUnlockRaritySixSlotResponse]):
	unit_id: int = None
	slot_id: int = None
	current_gold_num: int = None
	slot_list: List[PostMultiUnlockRarity6Slot] = None
	@property
	def url(self) -> str:
		return "unit/multi_unlock_rarity_6_slot"
class ChangeRarityRequest(Request[ChangeRarityResponse]):
	change_rarity_unit_list: List[ChangeRarityUnit] = None
	@property
	def url(self) -> str:
		return "unit/change_rarity"
class UnitFreeAutomaticEnhanceRequest(Request[UnitFreeAutomaticEnhanceResponse]):
	unit_id: int = None
	after_level: int = None
	equip_slot_num_list: List[int] = None
	skill_levelup_list: List[SkillLevelUpDetail] = None
	excludes_equip: int = None
	@property
	def url(self) -> str:
		return "unit/free_automatic_enhance"
class UnitFreeEquipRequest(Request[UnitFreeEquipResponse]):
	unit_id: int = None
	equip_slot_num_list: List[int] = None
	@property
	def url(self) -> str:
		return "unit/free_equip"
class UnitFreeEvolutionRequest(Request[UnitFreeEvolutionResponse]):
	unit_id: int = None
	current_unit_rarity: int = None
	@property
	def url(self) -> str:
		return "unit/free_evolution"
class UnitFreeMultiEvolutionRequest(Request[UnitFreeMultiEvolutionResponse]):
	unit_id: int = None
	current_rarity: int = None
	after_rarity: int = None
	@property
	def url(self) -> str:
		return "unit/free_multi_evolution"
class UnitFreeLevelUpRequest(Request[UnitFreeLevelUpResponse]):
	unit_id: int = None
	after_level: int = None
	@property
	def url(self) -> str:
		return "unit/free_level_up"
class UnitFreePromotionRequest(Request[UnitFreePromotionResponse]):
	unit_id: int = None
	target_promotion_level: int = None
	@property
	def url(self) -> str:
		return "unit/free_promotion"
class UnitSetGrowthItemRequest(Request[UnitSetGrowthItemResponse]):
	unit_id: int = None
	item_id: int = None
	@property
	def url(self) -> str:
		return "unit/set_growth_item"
class UnitGrowthEnhanceRequest(Request[UnitGrowthEnhanceResponse]):
	unit_id: int = None
	target_promotion_level: int = None
	@property
	def url(self) -> str:
		return "unit/growth_enhance"
class VoteExecRequest(Request[VoteExecResponse]):
	vote_id: int = None
	unit_rarity: int = None
	unit_id: int = None
	@property
	def url(self) -> str:
		return "vote/exec"
class VoteTopRequest(Request[VoteTopResponse]):
	vote_id: int = None
	@property
	def url(self) -> str:
		return "vote/top"

# 布丁小游戏 Start

class PsyTopRequest(Request[PsyTopResponse]):
	from_system_id: int = 6001
	@property
	def url(self) -> str:
		return "psy/top"

class StartCookingRequest(Request[StartCookingResponse]):
	start_cooking_frame_id_list: list = None
	get_pudding_frame_id_list: list = []
	from_system_id: int = 6001
	@property
	def url(self) -> str:
		return "psy/start_cooking"

class GetPuddingRequest(Request[GetPuddingResponse]):
	frame_id_list: list = None
	from_system_id: int = 6001
	@property
	def url(self) -> str:
		return "psy/get_pudding"

class PsyReadDramaRequest(Request[PsyReadDramaResponse]):
	drama_id: int = None
	from_system_id: int = 6001
	@property
	def url(self) -> str:
		return "psy/read_drama"

# 布丁小游戏 End
