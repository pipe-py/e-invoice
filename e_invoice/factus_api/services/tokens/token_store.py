import time


class TokenManager:
    def __init__(self):
        self._tokens = {}
        self.expires_in_seconds = None

    def save_tokens(self, tokens: dict, expires_in):
        self._tokens = tokens
        self.expires_in_seconds = self._tokens[expires_in]
        self._tokens["expires_at"] = time.time() + self.expires_in_seconds


token_manager = TokenManager()
