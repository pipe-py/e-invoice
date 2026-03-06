"""Helpers to download and store catalogs from the remote API."""

from e_invoice.core.utils.constants import ENDPOINTS
from e_invoice.core.clients.generic_request import Generic
from e_invoice.core.clients.http_client import http_requests
from e_invoice.factus_api.services.tokens.token_store import token_manager


class Catalogs:
    """Fetch and cache catalog data from configured endpoints."""

    def __init__(self) -> None:
        """Create an empty catalogs container with the current access token."""
        self._catalogs: dict = {}
        self.access_token = token_manager._tokens["access_token"]

    def fetch_catalogs(self) -> None:
        """Download all catalogs defined in the ``ENDPOINTS`` configuration.

        The data is stored in the private ``_catalogs`` dictionary where
        each key is the catalog name and the value is the response body.
        """
        endpoint = ENDPOINTS.get("catalogs")
        data = Generic()
        header = data.generic_header(access_token=self.access_token)

        catalogs_key = list(endpoint)
        self._catalogs = {
            catalog: http_requests(method="GET", url=endpoint[catalog], headers=header)
            for catalog in endpoint
            if catalog in catalogs_key
        }
