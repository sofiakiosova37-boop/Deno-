import httpx

class BaseHttpClient:
    async def request(self, method, url, **kwargs):
        async with httpx.AsyncClient() as client:
            return await client.request(method, url, **kwargs)
        
class AuthProxy:
    def __init__(self, inner_client, auth_strategy):
        self._client = inner_client 
        self._strategy = auth_strategy

    async def request(self, method, url, **kwargs):
        kwargs = self._strategy.apply(kwargs)
        return await self._client.request(method, url, **kwargs)