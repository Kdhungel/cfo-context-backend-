"""
Demo Client Script

Fetches the CFO Context Snapshot from the local FastAPI backend
and prints it nicely formatted.
"""

import json
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

# --- Configuration ---
CLIENT_ID = "client_acme"
BASE_URL = f"http://127.0.0.1:8000/api/clients/{CLIENT_ID}/context"

# --- Fetch data from backend ---
try:
    req = Request(BASE_URL, headers={"Accept": "application/json"})
    with urlopen(req) as response:
        if response.status == 200:
            data = json.load(response)
            # Pretty-print the JSON
            print(json.dumps(data, indent=2))
        else:
            print(f"Error: Received status code {response.status}")
except HTTPError as e:
    print(f"HTTP error occurred: {e.code} {e.reason}")
except URLError as e:
    print(f"Failed to reach server: {e.reason}")
except Exception as e:
    print(f"Unexpected error: {e}")