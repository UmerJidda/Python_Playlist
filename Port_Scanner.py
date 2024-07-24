import socket
import sys
from datetime import datetime

#define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
	#translates hostname to ipv4
else:
	print("invalid number of arguments")
	print("syntax : python3 scanner.py <ip>")
	sys.exit()

#Make it prettyyyyy
print("-" * 20)
print(f"Scanning Target : {target}")
print("time started : " + str(datetime.now()))
print("-" * 20)

try:
	for port in range(50, 85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port))
		if result == 0:
			print(f"Port {port} is open")
		s.close()
except KeyboardInterrupt:
	print("\nExiting Program.")
	sys.exit()
except socket.gaierror:
	#get address info error
	print("\nHostname could not be resolved.")
	sys.exit()
except socket.error:
	print("\nServer not responding.")
	sys.exit()


#just a basic Port scanner for my practice