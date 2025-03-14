from abstractclasses.abstract_model_interface import AbstractModelInterface
from anthropic import Anthropic
from typing import Optional
from openai import OpenAI
import constants

class GPTModelInterface(AbstractModelInterface):
    def __init__(self, openai_api_key: str):
        self.client = OpenAI(api_key=openai_api_key)  

    def send_to_model(self, system_prompt: str, task: str) -> str:       
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": task}
                ],
                max_tokens= constants.MAX_GPT_TOKENS,
                temperature= constants.GPT_TEMPERATURE,
                n=1,
                stop=None
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error while communicating with OpenAI API: {e}")
            return None

class CLDModelInterface(AbstractModelInterface):
    def __init__(self, anthropic_api_key: str):
        self.client = Anthropic(api_key=anthropic_api_key)

    def send_to_model(self, system_prompt: str, task: str) -> Optional[str]:
        try:
            response = self.client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens= constants.MAX_CLAUDE_TOKENS,
                temperature= constants.CLAUDE_TEMPERATURE,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": task}
                ]
            )
            return response.content[0].text.strip()
        except Exception as e:
            print(f"Error while communicating with Claude API: {e}")
            return None
