from abc import ABC, abstractmethod

class AbstractModelInterface(ABC):
    @abstractmethod
    def send_to_model(self, task: str) -> str:
        pass

    @abstractmethod
    def interpret_result(self, result: str) -> str:
        pass
