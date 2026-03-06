from e_invoice.core.utils.constants import ENDPOINTS
from e_invoice.core.clients.generic_request import Generic
from e_invoice.core.clients.http_client import http_requests
from e_invoice.factus_api.services.tokens.token_store import token_manager


class Catalogs:
    def __init__(self):
        self._catalogs = {}
        self.access_token = token_manager._tokens["access_token"]

    def fetch_catalogs(self):
        endpoint = ENDPOINTS.get("catalogs")
        data = Generic()
        header = data.generic_header(access_token=self.access_token)

        catalogs_key = list(endpoint)
        self._catalogs = {
            catalog: http_requests(method="GET", url=endpoint[catalog], headers=header)
            for catalog in endpoint
            if catalog in catalogs_key
        }
