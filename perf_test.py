import asyncio
import sys

from tqdm.asyncio import tqdm
import aiohttp


async def fetch(session, url):
    data = {
        "url": 'http://nonexistent.com'
    }
    async with session.post(url, json=data) as response:
        return await response.text()


async def load_testing():
    # phase 1 - post requests to server
    frequency = 1/10
    async with aiohttp.ClientSession() as session:
        for _ in tqdm(range(10000)):
            frequency /= 1.1
            asyncio.create_task(fetch(session, 'http://146.185.241.218/set'))
            await asyncio.sleep(frequency)

        frequency = 1/10
        for i in tqdm(range(11000, 18000)):
            frequency /= 1.5
            asyncio.create_task(session.get(f'http://146.185.241.218/{i}'))
            await asyncio.sleep(frequency)


asyncio.run(load_testing())
