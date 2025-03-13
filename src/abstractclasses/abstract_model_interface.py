from abc import ABC, abstractmethod

class AbstractModelInterface(ABC):
    @abstractmethod
    def send_to_model(self, system_prompt: str,task: str) -> str:
        pass


