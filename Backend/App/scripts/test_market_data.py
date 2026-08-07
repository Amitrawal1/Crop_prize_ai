from app.services.agmarknet.client import AgmarknetClient

client = AgmarknetClient()

params = {
    "dashboard_name": "Price",
    "page": 1,
    "page_size": 10,
}

response = client.get_dashboard_data(params)

records = response["data"]["records"]

print(f"Total Records: {len(records)}")
print()

for record in records:
    print(record)
    