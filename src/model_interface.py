import openai
from abstractclasses.abstract_model_interface import AbstractModelInterface

class ModelInterface(AbstractModelInterface):
    def __init__(self, openai_api_key: str):
        openai.api_key = openai_api_key

    def send_to_model(self, task: str) -> str:
        try:
            response = openai.Completion.create(
                engine="gpt-4",  
                prompt=task,
                max_tokens=1500, 
                temperature=0.5,
                n=1,
                stop=None
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"Error while communicating with OpenAI API: {e}")
            return ""

    def interpret_result(self, result: str) -> str:
        return f"Structural Analysis Report:\n{result}"
