from sys import argv
import re

script, filename, keyword = argv
names = [keyword,'is','meow']
names ="ur"+names
print "%r" % names

with open(filename) as f:
    for line in f:
		print "%r" % line
		for name in names:
			m = re.findall(r'name',line)	
			if m:
				print(m)
print "Here's your file %r:" % filename
print "keyword is:", keyword
