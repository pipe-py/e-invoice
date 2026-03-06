"""Helpers to build common HTTP request parts."""


class Generic:
    """Create generic data for HTTP requests."""

    @staticmethod
    def generic_header(access_token: str):
        """Return a simple JSON header with bearer token.

        Args:
            access_token: The access token for the remote API.

        Returns:
            A dictionary with content type, authorization and accept headers.
        """
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json"
        }