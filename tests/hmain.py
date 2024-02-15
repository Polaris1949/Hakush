from hakush import HakushClient
from hakush.model import Item
import asyncio, aiofiles
from typing import Awaitable

async def save_task(id: int, aw: Awaitable[bytes]) -> None:
    async with aiofiles.open(f"{id}.webp", "wb") as fp:
        await fp.write(await aw)

async def main00() -> None:
    async with HakushClient() as client:
        changelog = await client.changelog()
        avatar_tasks = tuple(save_task(id, client.avatar_image(id)) for id in changelog.character)
        lightcone_tasks = tuple(save_task(id, client.lightcone_image(id)) for id in changelog.lightcone)
        await asyncio.gather(*avatar_tasks + lightcone_tasks)

async def main01() -> None:
    from PIL import Image
    from io import BytesIO
    async with HakushClient() as client:
        aid = input("Input AvatarID: ")
        im = await client.avatar_image(aid)
        Image.open(BytesIO(im)).show()

async def item_check_task(id: int, aw: Awaitable[Item]) -> int:
    return id if len((await aw).ReturnItemIDList) else 0

async def main02() -> None:
    async with HakushClient() as client:
        item_tasks = tuple(item_check_task(id, client.item(id)) for id in await client.item_index())
        results = list(filter(lambda x: bool(x), await asyncio.gather(*item_tasks)))
        print(results)

async def main03() -> None:
    async with HakushClient() as client:
        a = await client.monster_template(1004010)
        print(repr(a))

if __name__ == "__main__":
    asyncio.run(main00())
