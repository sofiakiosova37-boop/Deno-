from abc import ABC, abstractmethod
import httpx

class HttpClient(ABC):
    @abstractmethod
    async def request(self, method: str, url: str, **kwargs) -> httpx.Response:
        pass