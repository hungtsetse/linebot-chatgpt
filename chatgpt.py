import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


class ChatGPT:
    def __init__(self):
        self.model = os.getenv("OPENAI_MODEL", default = "gpt-3.5-turbo")
        #self.temperature = float(os.getenv("OPENAI_TEMPERATURE", default = 1))
        #self.frequency_penalty = float(os.getenv("OPENAI_FREQUENCY_PENALTY", default = 0))
        #self.presence_penalty = float(os.getenv("OPENAI_PRESENCE_PENALTY", default = 0))

    def get_response(self, message):
        completion = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": message}],
            #temperature=self.temperature,
            #frequency_penalty=self.frequency_penalty,
            #presence_penalty=self.presence_penalty,
        )
        return completion.choices[0].message.content.strip()
