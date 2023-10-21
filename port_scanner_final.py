# import required modules
import socket
import time
import os

# create a socket object with the specified address family (IPv4) and socket type (TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get the target IP address from the user
target = input('Which interface do you want to scan?: ')

# use the gethostbyname() method to convert the host name to its corresponding IP address
target_ip = socket.gethostbyname(target)
print('Starting scan on host:', target_ip)

# function to check if a port is open or closed
def port_scan(port):
    try:
        # try to connect to the target on the specified port using the socket object
        s.connect((target_ip, port))
        # if the connection is successful, return True indicating that the port is open
        return True
    except:
        # if the connection fails, return False indicating that the port is closed
        return False

# clear the console and display the target IP address
os.system('cls')
print('Scanning on host:', target_ip)

# prompt the user to choose between scanning a specific port or a range of ports
print("How do you wish to scan?")
print("1. Scan specific port")
print("2. Scan range")
ch=int(input("Enter choice:"))

# wait for 1 second and clear the console again
time.sleep(1)
os.system('cls')

# if the user chooses to scan a specific port
if ch==1:
    # get the port number from the user
    port = int(input("Enter the port number to be scanned: "))
    # start the timer
    start = time.time()
    # check if the specified port is open or closed using the port_scan() function
    if port_scan(port):
        print('Port', port, 'is open')
    else:
        print("Port", port, "is closed")

# if the user chooses to scan a range of ports
elif ch==2:
    # get the starting and ending port numbers from the user
    s_port = int(input("Enter the starting port to be scanned: "))
    l_port = int(input("Enter the last port to be scanned: "))
    # start the timer
    start = time.time()
    # iterate through each port in the specified range and check if it's open or closed using the port_scan() function
    for port in range(s_port, l_port+1):
        if port_scan(port):
            print(f'Port {port} is open')
        else:
            print(f'Port {port} is closed')

# calculate the time taken to complete the scan and display it to the user
end = time.time()
print(f'Time taken {end-start:.2f} seconds')
