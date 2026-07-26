import requests

url = "https://api.agmarknet.gov.in/v1/dashboard-filters/"

params = {
    "dashboard_name": "marketwise_price_arrival"
}

headers = {
    "accept": "application/json",
    "origin": "https://agmarknet.gov.in",
    "referer": "https://agmarknet.gov.in/",
    "user-agent": "Mozilla/5.0"
}

response = requests.get(url, params=params, headers=headers)

data = response.json()

filters = data["data"]



print("Total States:", len(filters["state_data"]))
print("Total Districts:", len(filters["district_data"]))
print("Total Markets:", len(filters["market_data"]))
print("Total Commodities:", len(filters["cmdt_data"]))
print("Total Varieties:", len(filters["variety_data"]))
print("Total Grades:", len(filters["grade_data"]))