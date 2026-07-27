import os
import logging
import requests

from dotenv import load_dotenv

load_dotenv()


class AgmarknetClient:

    def __init__(self) -> None:
        self.base_url = os.getenv("BASE_URL")

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

        logging.basicConfig(level=logging.INFO)

    def _request(
        self,
        method: str,
        endpoint: str,
        params: dict | None = None,
        json: dict | None = None,
    ) -> dict:

        url = f"{self.base_url}/{endpoint}"

        logging.info(f"{method} {url}")

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
            raise ValueError(f"Unsupported HTTP Method: {method}")

        response.raise_for_status()

        return response.json()

    def get_filters(self) -> dict:

        params = {
            "dashboard_name": "marketwise_price_arrival"
        }

        return self._request(
            method="GET",
            endpoint="dashboard-filters/",
            params=params,
        )

    def get_dashboard_data(self, payload: dict) -> dict:

        return self._request(
            method="POST",
            endpoint="dashboard-data/",
            json=payload,
        )
        
