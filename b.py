import re

str = 'purple alice-b@google.com, blah monkey bob@abc.com blah dishwasher'
match = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print match
print match[0]
print match[1]














    








































#def a(str):
#	for i in range(0,len(str)):
#		if str[i].isalpha():
#			if str[i-1] != '+' or str[i+1] != '+':
#				return 'false'
#	return 'True'
#
#print a("+a+b+c+")