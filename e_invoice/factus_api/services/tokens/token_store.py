import time


class TokenManager:
    def __init__(self):
        self._tokens = {}

    def save_tokens(self, tokens: dict):
        self._tokens = tokens
        expires_in_seconds = tokens["expires_in"]
        self._tokens["expires_in"] = time.time() + expires_in_seconds


token_manager = TokenManager()
