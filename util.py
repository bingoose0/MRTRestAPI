from typing import Union
import aiohttp

async def request_json(url: str, **kwargs) -> Union[list, dict]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, **kwargs) as resp:
            return await resp.json()
    
    