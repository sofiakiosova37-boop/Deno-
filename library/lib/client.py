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
    
class IssService:
    def __init__(self, http_client):
        self._http = http_client 
    async def get_data(self, url):
        response = await self._http.request("GET", url)
        return response.json()
    
class ApiKeyStrategy:
    def __init__(self, key):
        self.key = key
    def apply(self, kwargs):
        params = kwargs.get('params', {})
        params['api_key'] = self.key
        kwargs['params'] = params
        return kwargs