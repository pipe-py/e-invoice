"""Simple in-memory store for authentication tokens."""

import time


class TokenManager:
    """Manage access and refresh tokens with an expiration time."""

    def __init__(self) -> None:
        """Initialise an empty token dictionary."""
        self._tokens: dict = {}
        self.expires_in_seconds: float | None = None

    def save_tokens(self, tokens: dict, expires_in: str) -> None:
        """Save new tokens and compute their expiration time.

        Args:
            tokens: Dictionary with token data from the authentication API.
            expires_in: Key name in ``tokens`` that holds the lifetime in seconds.
        """
        self._tokens = tokens
        self.expires_in_seconds = self._tokens[expires_in]
        self._tokens["expires_at"] = time.time() + self.expires_in_seconds


token_manager = TokenManager()
