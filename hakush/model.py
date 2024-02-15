from pydantic import BaseModel
from typing import List, Dict, Optional, Any, Union


class HakushBaseModel(BaseModel):
    pass


class Changelog(HakushBaseModel):
    character: List[int]
    lightcone: List[int]
    relicset: List[int]
    version: str


class BriefAvatar(HakushBaseModel):
    icon: str
    rank: str
    baseType: str
    damageType: str
    en: str
    desc: str
    kr: str
    cn: str
    jp: str


class AvatarVoice(HakushBaseModel):
    VoiceID: int
    VoiceTitle: str
    VoiceM: str
    UnlockDesc: Optional[str]
    IsBattleVoice: bool


class AvatarFetter(HakushBaseModel):
    Camp: str
    VA: Dict[str, str]
    Stories: Dict[int, str]
    Voicelines: List[AvatarVoice]


class AvatarRank(HakushBaseModel):
    Id: int
    Name: str
    Desc: str
    ParamList: List[float]


class AvatarSkillLevel(HakushBaseModel):
    Level: int
    ParamList: List[float]


class AvatarSkill(HakushBaseModel):
    Name: str
    Desc: str
    Type: Optional[str]
    Tag: str
    SPBase: Optional[int]
    ShowStanceList: List[int]
    SkillComboValueDelta: Optional[int]
    Level: Dict[int, AvatarSkillLevel]


class ItemPair(HakushBaseModel):
    ItemID: int
    ItemNum: int


class PropertyPair(HakushBaseModel):
    PropertyType: str
    Value: float


class AvatarSkillTree(HakushBaseModel):
    Anchor: str
    AvatarPromotionLimit: Optional[int]
    AvatarLevelLimit: Optional[int]
    DefaultUnlock: bool
    Icon: str
    LevelUpSkillID: List[int]
    MaterialList: List[ItemPair]
    MaxLevel: int
    ParamList: List[float]
    PointID: int
    PointName: Optional[str]
    PointDesc: Optional[str]
    PointTriggerKey: int
    PointType: int
    PrePoint: List[int]
    StatusAddList: List[PropertyPair]


class AvatarPromotion(HakushBaseModel):
    AttackBase: float
    AttackAdd: float
    DefenceBase: float
    DefenceAdd: float
    HPBase: float
    HPAdd: float
    SpeedBase: int
    CriticalChance: float
    CriticalDamage: float
    BaseAggro: int
    Cost: List[ItemPair]


class RelicPropertyPair(HakushBaseModel):
    PropertyType: str
    RelicType: str


class AvatarRelicRecommend(HakushBaseModel):
    AvatarID: int
    PropertyList: List[RelicPropertyPair]
    Set2IDList: List[int]
    Set4IDList: List[int]


class Avatar(HakushBaseModel):
    Name: str
    Desc: str
    CharaInfo: AvatarFetter
    Rarity: str
    AvatarVOTag: str
    SPNeed: int
    BaseType: str
    DamageType: str
    Ranks: Dict[int, AvatarRank]
    Skills: Dict[int, AvatarSkill]
    SkillTrees: Dict[str, Dict[int, AvatarSkillTree]]
    Stats: Dict[int, AvatarPromotion]
    Relics: AvatarRelicRecommend


class BriefLightcone(HakushBaseModel):
    rank: str
    baseType: str
    en: str
    desc: str
    kr: str
    cn: str
    jp: str


class LightconeSkillLevel(HakushBaseModel):
    ParamList: List[float]


class LightconeSkill(HakushBaseModel):
    Name: str
    Desc: str
    Level: Dict[int, LightconeSkillLevel]


class LightconePromotion(HakushBaseModel):
    BaseAttack: float
    BaseAttackAdd: float
    BaseDefence: float
    BaseDefenceAdd: float
    BaseHP: float
    BaseHPAdd: float
    EquipmentID: int
    MaxLevel: int
    Promotion: Optional[int] = None
    PlayerLevelRequire: Optional[int] = None
    PromotionCostList: List[ItemPair]
    WorldLevelRequire: Optional[int] = None


class Lightcone(HakushBaseModel):
    Name: str
    Desc: str
    Rarity: str
    BaseType: str
    Refinements: LightconeSkill


class BriefRelicSetDesc(HakushBaseModel):
    en: str
    ParamList: List[float]
    kr: str
    cn: str
    jp: str


class BriefRelicSet(HakushBaseModel):
    icon: str
    en: str
    set: Dict[int, BriefRelicSetDesc]
    kr: str
    cn: str
    jp: str


class Relic(HakushBaseModel):
    Name: str
    Desc: str
    Story: str


class RelicSetSkill(HakushBaseModel):
    Desc: str
    ParamList: List[float]


class RelicSet(HakushBaseModel):
    Name: str
    Icon: str
    Parts: Dict[int, Relic]
    RequireNum: Dict[int, RelicSetSkill]


class Achievement(HakushBaseModel):
    Id: int
    Name: str
    Desc: str
    ParamList: List[float]
    Rarity: str
    ShowType: str


class AchievementSeries(HakushBaseModel):
    Id: int
    Priority: int
    Name: str
    List: List[Achievement]


class BriefItem(HakushBaseModel):
    ItemName: str
    ItemSubType: str
    Rarity: str
    ItemFigureIconPath: str


class ItemComefrom(HakushBaseModel):
    ID: int
    Desc: str


class Item(HakushBaseModel):
    ID: int
    ItemMainType: str
    ItemSubType: str
    InventoryDisplayTag: int
    Rarity: str
    PurposeType: Optional[int] = None
    ItemName: str
    ItemDesc: str
    ItemBGDesc: str
    ItemIconPath: str
    ItemFigureIconPath: str
    ItemCurrencyIconPath: str
    ItemAvatarIconPath: str
    PileLimit: int
    UseMethod: Optional[str] = None
    UseDataID: Optional[int] = None
    CustomDataList: List[int]
    ReturnItemIDList: List[Any]  # Always []
    ItemGroup: Optional[int] = None
    SellType: Optional[str] = None
    ItemComefrom: List[ItemComefrom]


class BriefMonster(HakushBaseModel):
    rank: str
    camp: Optional[int]
    icon: str
    child: List[int]
    weak: List[str]
    en: str
    desc: str
    kr: str
    cn: str
    jp: str


class ElementResistance(HakushBaseModel):
    DamageType: str
    Value: float


class MonsterSkill(HakushBaseModel):
    Id: int
    SkillName: str
    SkillDesc: str
    DamageType: str
    SPHitBase: Union[float, str] # Sometimes ""


class Monster(HakushBaseModel):
    Id: int
    AttackModifyRatio: float
    DefenceModifyRatio: float
    EliteGroup: int
    HPModifyRatio: float
    SpeedModifyRatio: float
    SpeedModifyValue: Optional[float]
    StanceModifyRatio: float
    StanceWeakList: List[str]
    HardLevelGroup: int
    DamageTypeResistance: List[ElementResistance]
    SkillList: List[MonsterSkill]


class ItemDrop(HakushBaseModel):
    ID: int


class MonsterDrop(HakushBaseModel):
    MonsterTemplateID: int
    WorldLevel: Optional[int] = None
    AvatarExpReward: Optional[int] = None
    DisplayItemList: List[ItemDrop]


class MonsterTemplate(HakushBaseModel):
    Id: int
    Name: str
    Desc: str
    MonsterCampID: Optional[int]
    AttackBase: float
    CriticalDamageBase: float
    DefenceBase: float
    HPBase: float
    InitialDelayRatio: float
    ImagePath: str
    MinimumFatigueRatio: float
    Rank: str
    SpeedBase: float
    StanceBase: float
    StanceCount: int
    StatusResistanceBase: float
    Child: List[Monster]
    Drop: List[MonsterDrop]
