import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
DASHBOARD_NAME = os.getenv("DASHBOARD_NAME")

if BASE_URL is None:
    raise RuntimeError("BASE_URL not found.")

if DASHBOARD_NAME is None:
    raise RuntimeError("DASHBOARD_NAME not found.")