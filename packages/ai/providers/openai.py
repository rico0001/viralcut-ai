from typing import Any, Dict
import openai

class OpenAIProvider:
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        self.api_key = api_key
        self.model = model
        openai.api_key = self.api_key

    def generate_highlight(self, prompt: str) -> Dict[str, Any]:
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']

    def generate_metadata(self, prompt: str) -> Dict[str, Any]:
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']

    def generate_captions(self, transcript: str) -> str:
        prompt = f"Generate captions for the following transcript:\n{transcript}"
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']