import json
import requests
import os

HOST = os.environ["DATABRICKS_HOST"]
TOKEN = os.environ["DATABRICKS_TOKEN"]

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

with open("jobs/ingest-process-pipeline.json", "r") as f:
    job_config = json.load(f)

response = requests.post(
    f"{HOST}/api/2.1/jobs/create",
    headers=headers,
    json=job_config
)

print(response.status_code)
print(response.text)