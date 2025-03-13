from abc import ABC, abstractmethod

class AbstractTaskPackager(ABC):
    @abstractmethod
    def package_task(self,user_input: str) -> str:
        pass
