from abc import ABC, abstractmethod

class AbstractResponseRetriever(ABC):
    @abstractmethod
    def parse_response(self, response: str) -> str:
        pass
