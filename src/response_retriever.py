import re
from abstractclasses.abstract_response_retriever import AbstractResponseRetriever

class BackTicksResponseRetriever(AbstractResponseRetriever):
    def __init__(self):
        pass

    def parse_response(self, response: str) -> str:
        code_pattern = re.compile(r'```(.*?)```', re.DOTALL) 
        matches = code_pattern.findall(response)
        if matches:
            return matches[0]
        else:
            return None
