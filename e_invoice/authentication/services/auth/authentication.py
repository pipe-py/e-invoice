from e_invoice.core.utils.constants import ENDPOINTS
from e_invoice.core.clients.http_client import http_requests
from e_invoice.authentication.services.schemas.auth_config import OAuth2Credentials


def authentication() -> dict:
    data = OAuth2Credentials()
    endpoint = ENDPOINTS["authentication"]["endpoint"]
    payload = data.payload()
    header = data.header()

    return http_requests(method="POST", url=endpoint, data=payload, headers=header)
