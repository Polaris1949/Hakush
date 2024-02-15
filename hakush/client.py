from types import TracebackType
from typing import Dict, Optional, Type, Union

import aiohttp

from .error import HakushError
from .model import (
    Changelog,
    BriefAvatar,
    Avatar,
    BriefLightcone,
    Lightcone,
    BriefRelicSet,
    RelicSet,
    AchievementSeries,
    BriefItem,
    Item,
    BriefMonster,
    MonsterTemplate,
)
from .typedef import Json


class HakushClient:
    def __init__(self) -> None:
        self.session = aiohttp.ClientSession(
            "https://api.hakush.in", connector=aiohttp.TCPConnector(limit=16)
        )

    async def close(self) -> None:
        await self.session.close()

    async def __aenter__(self) -> "HakushClient":
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        await self.session.close()

    async def get(self, url: str, **kwargs) -> bytes:
        async with self.session.get(url, **kwargs) as resp:
            if resp.status != 200:
                raise HakushError(f"{resp.status} {resp.reason}", url)
            return await resp.read()

    async def get_json(self, url: str, **kwargs) -> Json:
        async with self.session.get(url, **kwargs) as resp:
            if resp.status != 200:
                raise HakushError(f"{resp.status} {resp.reason}", url)
            return await resp.json()

    async def changelog(self) -> Changelog:
        return Changelog(**(await self.get_json("/hsr/new.json")))

    async def avatar_index(self) -> Dict[int, BriefAvatar]:
        return {
            int(key): BriefAvatar(**value)
            for key, value in (await self.get_json("/hsr/data/character.json")).items()
        }

    async def avatar(self, id: Union[int, str]) -> Avatar:
        return Avatar(**(await self.get_json(f"/hsr/data/cn/character/{id}.json")))

    async def lightcone_index(self) -> Dict[int, BriefLightcone]:
        return {
            int(key): BriefLightcone(**value)
            for key, value in (await self.get_json("/hsr/data/lightcone.json")).items()
        }

    async def lightcone(self, id: Union[int, str]) -> Lightcone:
        return Lightcone(**(await self.get_json(f"/hsr/data/cn/lightcone/{id}.json")))

    async def relicset_index(self) -> Dict[int, BriefRelicSet]:
        return {
            int(key): BriefRelicSet(**value)
            for key, value in (await self.get_json("/hsr/data/relicset.json")).items()
        }

    async def relicset(self, id: Union[int, str]) -> RelicSet:
        return RelicSet(**(await self.get_json(f"/hsr/data/cn/relicset/{id}.json")))

    async def achievement_index(self) -> Dict[int, AchievementSeries]:
        return {
            int(key): AchievementSeries(**value)
            for key, value in (await self.get_json("/hsr/live/cn/achievement/achievement.json")).items()
        }

    async def item_index(self) -> Dict[int, BriefItem]:
        return {
            int(key): BriefItem(**value)
            for key, value in (await self.get_json("/hsr/data/cn/item.json")).items()
        }

    async def item(self, id: Union[int, str]) -> Item:
        return Item(**(await self.get_json(f"/hsr/data/cn/item/{id}.json")))

    async def monster_index(self) -> Dict[int, BriefMonster]:
        return {
            int(key): BriefMonster(**value)
            for key, value in (await self.get_json("/hsr/data/monster.json")).items()
        }

    async def monster_template(self, id: Union[int, str]) -> MonsterTemplate:
        return MonsterTemplate(**(await self.get_json(f"/hsr/data/cn/monster/{id}.json")))

    async def avatar_icon(self, id: Union[int, str]) -> bytes:
        return await self.get(f"/hsr/UI/avatarroundicon/{id}.webp")

    async def avatar_icon_shop(self, id: Union[int, str]) -> bytes:
        return await self.get(f"/hsr/UI/avatarshopicon/{id}.webp")

    async def avatar_image(self, id: Union[int, str]) -> bytes:
        return await self.get(f"/hsr/UI/avatardrawcard/{id}.webp")

    async def avatar_rank_image(self, id: Union[int, str]) -> bytes:
        # Exmaple: id=121204
        if isinstance(id, int):
            aid = id // 100
            rid = id % 100
        else:
            aid = id[:4]
            rid = id[5]
        return await self.get(
            f"/hsr/UI/rank/_dependencies/textures/{aid}/{aid}_Rank_{rid}.webp"
        )

    async def lightcone_icon_medium(self, id: Union[int, str]) -> bytes:
        return await self.get(f"/hsr/UI/lightconemediumicon/{id}.webp")

    async def lightcone_image(self, id: Union[int, str]) -> bytes:
        return await self.get(f"/hsr/UI/lightconemaxfigures/{id}.webp")

    async def relicset_icon(
        self, id: Union[int, str, BriefRelicSet, RelicSet]
    ) -> bytes:
        # Example: id=101
        if isinstance(id, BriefRelicSet):
            iid = id.icon
        else:
            if not isinstance(id, RelicSet):
                id = await self.relicset(id)
            iid = id.Icon
        iid = iid[22:27]
        return await self.get(f"/hsr/UI/itemfigures/{iid}.webp")

    async def relic_icon(self, id: Union[int, str]) -> bytes:
        # Example: id=31011
        if isinstance(id, int):
            sid = id // 10 % 1000
            pid = id % 10
        else:
            sid = id[1:4]
            pid = id[4]
        return await self.get(f"/hsr/UI/relicfigures/IconRelic_{sid}_{pid}.webp")

    async def item_icon(self, id: Union[int, str]) -> bytes:
        return await self.get(f"/hsr/UI/itemfigures/{id}.webp")

    async def profession_icon(self, name: str) -> bytes:
        # Lower case, e.g. rogue.
        return await self.get(f"/hsr/UI/pathicon/{name}.webp")

    async def attribute_icon(self, name: str) -> bytes:
        # Lower case, e.g. quantum.
        return await self.get(f"/hsr/UI/element/{name}.webp")

    async def status_icon(self, name: str) -> bytes:
        # Original case, e.g. MaxHP.
        return await self.get(f"/hsr/UI/trace/Icon{name}.webp")
