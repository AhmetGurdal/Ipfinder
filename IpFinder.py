import os
from sys import argv
import time
ip = ""
ips = []
difips = []
def isip(ip, ips):
	sip = ip
	while True:
		if "." in sip:
			first = sip[ : sip.find(".")]
			if len(first) >= 4:
				ip = ""
				break
			else:
				sip = sip[sip.find(".") + 1:]
		else:
			if ip != "":
				ips.append(ip)
				break
	
				
if len(argv) >= 2:	
	file = open(argv[1],"r")
	file = file.read()
	
	for i in file:
		if i.isdigit() == True:
			ip = ip + i
		elif i == ".":
			ip = ip + "."
		else:
			if len(ip)>0 and ip.count(".") == 3 and len(ip) <= 15 and ip[len(ip) - 1].isdigit() == True and len(ip[len(ip) - 1]) <= 3:
				if ip[len(ip)-2] == "." or ip[len(ip)-3] == "." or ip[len(ip)-4] == ".":
					isip(ip,ips)
			ip = ""
	if len(ip) > 0 and ip.count(".") == 3 and len(ip) <= 15 and ip[len(ip) - 1].isdigit() == True and len(ip[len(ip) - 1]) <= 3:
		if ip[len(ip)-2] == "." or ip[len(ip)-3] == "." or ip[len(ip)-4] == ".":
			isip(ip,ips)
			
else:
	print "ipfinder.py <path>"
	
for i in ips:
	if i not in difips:
		difips.append(i)

for i in difips:
	print i + " -- " + str(ips.count(i))
