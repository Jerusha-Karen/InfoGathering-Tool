import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <url>")
    sys.exit(1)

url = sys.argv[1]

try:
    # Fetch HTTP Headers
    req = requests.get("https://" + url)
    print("\nHTTP Headers:\n", req.headers)

    # Get IP Address of the URL
    ip_address = socket.gethostbyname(url)
    print("\nThe IP address of " + url + " is: " + ip_address + "\n")

    # Fetch Geolocation Data
    req_two = requests.get("https://ipinfo.io/" + ip_address + "/json")
    resp_ = json.loads(req_two.text)

    # Corrected dictionary access using .get() to avoid KeyError
    print("Location: " + resp_.get("loc", "N/A"))
    print("Region: " + resp_.get("region", "N/A"))
    print("Country: " + resp_.get("country", "N/A"))
    print("ISP: " + resp_.get("org", "N/A"))
    print("City: " + resp_.get("city", "N/A"))

except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
except socket.gaierror:
    print("Error: Invalid URL or domain not found.")
