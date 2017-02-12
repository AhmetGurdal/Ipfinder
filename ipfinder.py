import re
from sys import argv

print argv

if (argv)
f = open("ip.txt","r")

best = re.findall(r'\d{1,4}\.\d{1,3}\.\d{1,3}\.\d{1,4}',f.read())

excellent = []
lookslike = []

for i in best:
	c = True
	
	if len(i.split(".")) > 4:
		c = False
	if c:
		for j in i.split("."):
			if int(j) > 255:
				c = False
				break
	if c:
		excellent.append(i)

	else:
		lookslike.append(i)
print "----------------------"
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
