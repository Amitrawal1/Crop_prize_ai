import logging

import requests

from app.core.config import BASE_URL, DASHBOARD_NAME

logger = logging.getLogger(__name__)


class AgmarknetClient:

    def __init__(self) -> None:
        self.base_url = BASE_URL

        self.headers = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "origin": "https://agmarknet.gov.in",
            "referer": "https://agmarknet.gov.in/",
            "user-agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/149.0.0.0 Safari/537.36"
            ),
        }

    def _request(
        self,
        method: str,
        endpoint: str,
        params: dict | None = None,
        json: dict | None = None,
    ):

        url = f"{self.base_url}/{endpoint}"

        logger.info(f"{method} {url}")

        if method == "GET":

            response = requests.get(
                url,
                headers=self.headers,
                params=params,
                timeout=30,
            )

        elif method == "POST":

            response = requests.post(
                url,
                headers=self.headers,
                json=json,
                timeout=30,
            )

        else:
            raise ValueError(f"Unsupported method: {method}")

        response.raise_for_status()

        data = response.json()

        if "status" not in data:
            raise ValueError("Missing 'status' in API response.")

        if "data" not in data:
            raise ValueError("Missing 'data' in API response.")

        return data

    def get_filters(self):

        params = {
            "dashboard_name": DASHBOARD_NAME,
        }

        return self._request(
            method="GET",
            endpoint="dashboard-filters/",
            params=params,
        )

    def build_dashboard_payload(
        self,
        date: str,
        group: list[int],
        commodity: list[int],
        variety: int,
        state: int,
        district: list[int],
        market: list[int],
        grades: list[int],
        limit: int = 10,
    ) -> dict:

        return {
            "dashboard": DASHBOARD_NAME,
            "date": date,
            "group": group,
            "commodity": commodity,
            "variety": variety,
            "state": state,
            "district": district,
            "market": market,
            "grades": grades,
            "limit": limit,
            "format": "json",
        }

    def get_dashboard_data(
        self,
        payload: dict,
    ):

        return self._request(
            method="POST",
            endpoint="dashboard-data/",
            json=payload,
        )