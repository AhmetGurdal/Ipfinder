import re
import sys

f = open("ip.txt","r")

a = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^\.]',f.read())
excellent = []
lookslike = []
for i in a:
	c = True
	for j in i.split("."):
		
		if int(j) > 255:
			c = False

	if c:
		excellent.append(i[:-1])

	else:
		lookslike.append(i[:-1])

print "Most probably IP addresses"
again = []
if len(excellent) > 0:
	for  i in excellent:
		if i not in again:
			print '-> ' + i + ' is counted ' + str(excellent.count(i)) + " times."
			again.append(i)
else:
	print "Couldn't find a valid IP address."
again = []
if len(lookslike) > 0:
	print "Less probably IP addresses"
	for  i in lookslike:
		if i not in again:
			print "-> " + i + " is counted " + str(lookslike.count(i)) + " times."
