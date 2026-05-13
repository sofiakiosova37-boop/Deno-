import httpx

class BaseHttpClient:
    async def request(self, method, url, **kwargs):
        async with httpx.AsyncClient() as client:
            return await client.request(method, url, **kwargs)