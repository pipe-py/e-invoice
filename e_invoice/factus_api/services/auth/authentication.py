from e_invoice.core.utils.constants import ENDPOINTS
from e_invoice.core.clients.http_client import http_requests
from e_invoice.factus_api.services.schemas.auth_config import (
    OAuth2Credentials,
    RefreshToken,
)
from e_invoice.factus_api.services.tokens.token_store import token_manager


def authentication() -> dict:
    data = OAuth2Credentials()
    endpoint = ENDPOINTS["authentication"]["endpoint"]
    payload = data.payload()
    header = data.header()

    response = http_requests(method="POST", url=endpoint, data=payload, headers=header)

    token_manager.save_tokens(tokens=response, expires_in="expires_in")


def refresh_token() -> dict:
    data = RefreshToken()
    endpoint = ENDPOINTS["refreshToken"]["endpoint"]
    payload = data.payload()
    header = data.header(token=token_manager._tokens["access_token"])

    response = http_requests(method="POST", url=endpoint, data=payload, headers=header)

    token_manager.save_tokens(tokens=response, expires_in="expires_in")
