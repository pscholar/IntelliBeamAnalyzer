from abc import ABC, abstractmethod

class AbstractInstructionRunner(ABC):
    @abstractmethod
    def save_and_run(self, code: str, output_file: str = None) -> str:
        pass
