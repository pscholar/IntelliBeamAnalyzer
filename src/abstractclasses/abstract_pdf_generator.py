from abc import ABC, abstractmethod

class AbstractPDFGenerator(ABC):
    @abstractmethod
    def generate_pdf(self, content: str = None, file_name: str = None, 
                     format_flag: str = 'html', output_pdf: str = None) -> str:
        pass

