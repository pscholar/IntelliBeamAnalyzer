import re
from abstractclasses.abstract_response_retriever import AbstractResponseRetriever

class BackTicksResponseRetriever:
    def __init__(self):
        pass

    def parse_response(self, response: str) -> str:
        code_pattern = re.compile(r'```(?:\w+)?\n(.*?)```', re.DOTALL)
        matches = code_pattern.findall(response)
        if matches:
            #print(matches[0].strip())
            return matches[0].strip()  
        else:
            return None

