import re
from sys import argv
import sys


def writeAll():
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


def help():
	print "Help line"
	print "-f \t-> For give file name"
	print "-F \t-> For give file names file"
	print "-l \t-> give specific ip address."
	print "-L \t-> give specific ip addresses file."


if ("-f" in argv):
	fl = argv[argv.index("-f")+1]
try:
	f = open(fl,"r")
except:
	help()
	sys.exit(1)
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


if ("-l" in argv):
	
	if (argv[argv.index("-l")+1] in excellent):
		print argv[argv.index("-l")+1] + " is counted " + str(excellent.count(argv[argv.index("-l")+1])) + " times"
	if (argv[argv.index("-l")+1] in lookslike):
		print argv[argv.index("-l"+1)] + " is counted " + str(lookslike.count(argv[argv.index("-l")+1])) + " times"
if ("-l" not in argv):
	writeAll()