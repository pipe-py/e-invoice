"""Functions to authenticate and refresh tokens with the remote API."""

from e_invoice.core.utils.constants import ENDPOINTS
from e_invoice.core.clients.http_client import http_requests
from e_invoice.factus_api.services.schemas.auth_config import (
    OAuth2Credentials,
    RefreshToken,
)
from e_invoice.factus_api.services.tokens.token_store import token_manager


def authentication() -> dict:
    """Request a new access token using user credentials.

    The function reads credentials from environment variables through
    the ``OAuth2Credentials`` settings model and stores the received
    tokens in the shared ``token_manager`` instance.

    Returns:
        The token response body as a dictionary.
    """
    data = OAuth2Credentials()
    endpoint = ENDPOINTS["authentication"]["endpoint"]
    payload = data.payload()
    header = data.header()

    response = http_requests(method="POST", url=endpoint, data=payload, headers=header)

    token_manager.save_tokens(tokens=response, expires_in="expires_in")
    return response


def refresh_token() -> dict:
    """Request a new access token using a refresh token.

    The function uses the current refresh token stored in ``token_manager``
    and updates the shared token store when the call is successful.

    Returns:
        The token response body as a dictionary.
    """
    data = RefreshToken()
    endpoint = ENDPOINTS["refreshToken"]["endpoint"]
    payload = data.payload()
    header = data.header(token=token_manager._tokens["access_token"])

    response = http_requests(method="POST", url=endpoint, data=payload, headers=header)

    token_manager.save_tokens(tokens=response, expires_in="expires_in")
    return response
