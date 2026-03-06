"""Small HTTP client wrapper for the e-invoice service."""

import time
import requests
from typing import Literal


def http_requests(
    method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"],
    url: str,
    params: dict | None = None,
    data: dict | None = None,
    headers: dict | None = None,
    timeout: int = 5,
) -> dict:
    """Send an HTTP request and return the JSON body.

    This function uses the ``requests`` library with a simple interface.

    Args:
        method: HTTP method name like ``"GET"`` or ``"POST"``.
        url: Full URL for the request.
        params: Optional query parameters.
        data: Optional request body as a dictionary.
        headers: Optional HTTP headers.
        timeout: Request timeout in seconds.

    Returns:
        The decoded JSON body as a dictionary when the status code is 200.
        When the status code is not 200, the returned value is undefined.
    """

    response = requests.request(
        method=method,
        url=url,
        params=params,
        data=data,
        headers=headers,
        timeout=timeout,
    )

    if response.status_code == 200:
        data = response.json()
    return data
