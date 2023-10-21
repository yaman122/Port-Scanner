# Port-Scanner
# Port Scanner

This simple Python script scans for open ports on a specified host using the socket library.

## Usage

1. **Run the script:**
   ```bash
   python port_scanner.py
Enter the target host: Provide the host (IP address or domain) when prompted.

Choose scanning method:

Scan specific port: Enter the port number to check if it's open or closed.
Scan port range: Enter the starting and ending port numbers.
View results: The script will display the status (open/closed) of each port.

View scan duration: The time taken for the scan is shown at the end.

Example
bash
Copy code
Which interface do you want to scan?: example.com
Starting scan on host: 93.184.216.34

How do you wish to scan?
1. Scan specific port
2. Scan range
Enter choice: 1

Enter the port number to be scanned: 80
Port 80 is open
Time taken 1.23 seconds

Requirements
Python 3.x

Compatible with Windows and Unix-based systems.

Disclaimer
This script is for educational purposes. Ensure proper authorization before scanning any network. The author is not responsible for any misuse or damage.
