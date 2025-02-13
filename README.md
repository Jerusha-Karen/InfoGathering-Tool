
🔍Information Gathering Tool

A simple yet powerful Information Gathering Tool written in Python. This tool fetches essential data about a given website, including HTTP headers, IP addresses, and geolocation details.

🚀 Features

Fetches HTTP headers of a website.

Resolves domain names to IP addresses.

Retrieves geolocation details (City, Region, Country, ISP) using ipinfo.io.

Error handling for invalid domains and network issues.

🛠️ Installation

Ensure you have Python installed. Then, install the required dependencies:

pip install requests

📌 Usage

Run the script with a domain name:

python tool.py google.com

✅ Example Output

HTTP Headers:
{'Date': 'Thu, 13 Feb 2025 18:25:25 GMT', 'Content-Type': 'text/html', ...}

The IP address of google.com is: 142.250.193.142

Location: 13.0878,80.2785
Region: Tamil Nadu
Country: IN
ISP: AS15169 Google LLC
City: Chennai

🔧 Error Handling

Invalid URL? The script will notify you.

Network issues? The script will handle them gracefully.

🤝 Contributing

Feel free to fork this project, improve it, and submit a pull request!
