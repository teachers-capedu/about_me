import os
from dotenv import load_dotenv
import requests
from pathlib import Path

load_dotenv("source.env")


HOSTNAME = os.getenv("HOSTNAME")
EMAIL    = os.getenv("EMAIL")
APIKEY   = os.getenv("API_KEY")


resp = requests.post(
    f"https://{HOSTNAME}/v2api/auth/login",
    json={
        "email": EMAIL,
        "api_key": APIKEY
    }
)
print("Статус:", resp.status_code)
print("Ответ:", resp.text[:300])
