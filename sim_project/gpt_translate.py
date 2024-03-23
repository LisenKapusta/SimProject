import os
from typing import Tuple

import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

class SimlishTranslate:
    def __init__(self):
        self._prompt = """
        Ты должен переводить входящий текст имитируя язык из серии игр The Sims
        """
        self._prompt_2 = """Commit Message Generator is ready."""
        self._model_name = "gpt-3.5-turbo"

    def predict(self, diff: str) -> Tuple[str, str]:
        message_history = [
            {"role": "user", "content": self._prompt},
            {"role": "assistant", "content": self._prompt_2},
            {
                "role": "user",
                "content": f"{diff}",
            },
        ]
        assistant_message = openai.ChatCompletion.create(
            model=self._model_name,
            messages=message_history,
        )["choices"][0]["message"]["content"].replace("Output:", "", 1)
        type = str(assistant_message.split("]")[0].replace("[", ""))
        message = str(assistant_message.split("]")[1].strip())
        return type, message

    def __call__(
            self,
            diff: str,
    ) -> Tuple[str, str]:
        """
        Generate commit message from diff.

        Args:
            diff: Diff to generate commit message from.

        Returns:
            Tuple of commit message type and commit message.
        """
        return self.predict(diff)