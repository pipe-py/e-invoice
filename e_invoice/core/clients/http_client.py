import time
import requests
from typing import Literal


def http_requests(
    method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"],
    url: str,
    params: dict = None,
    data: dict = None,
    headers: dict = None,
    timeout=5,
) -> dict:

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
