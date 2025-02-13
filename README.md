
<h2>🔍Information Gathering Tool</h2>

A simple yet powerful Information Gathering Tool written in Python. This tool fetches essential data about a given website, including HTTP headers, IP addresses, and geolocation details.

<h4>🚀 Features</h4>

Fetches HTTP headers of a website.

Resolves domain names to IP addresses.

Retrieves geolocation details (City, Region, Country, ISP) using ipinfo.io.

Error handling for invalid domains and network issues.

<h4>🛠️ Installation</h4>

Ensure you have Python installed. Then, install the required dependencies:

pip install requests


<h4>📌 Usage</h4>

Run the script with a domain name:

python tool.py google.com

<h4>✅ Example Output</h4>

HTTP Headers:
{'Date': 'Thu, 13 Feb 2025 18:25:25 GMT', 'Content-Type': 'text/html', ...}

The IP address of google.com is: 142.250.193.142

Location: 13.0878,80.2785<br>
Region: Tamil Nadu<br>
Country: IN<br>
ISP: AS15169 Google LLC<br>
City: Chennai<br>

<h4>🔧 Error Handling</h4>

Invalid URL? The script will notify you.

Network issues? The script will handle them gracefully.

<h4>🤝 Contributing

Feel free to fork this project, improve it, and submit a pull request!
