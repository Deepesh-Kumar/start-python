import pexpect
import sys

x = raw_input('Enter IP: ')
y = raw_input('Enter username: ')
z = raw_input('Enter password: ')



try:
	c = pexpect.spawn('ssh %s@%s' %(y,x))
	c.timeout = 4
	c.expect("password: ")
	c.logfile = sys.stdout
except pexpect.TIMEOUT:
	raise Exception("Fail")

c.sendline(z)
c.expect("vManage1#")
c.sendline("show software")
c.expect("# ")
c.sendline("show version")
c.expect("# ")
c.sendline("show control valid-vedges")
c.expect("# ")
c.sendline("request execute ssh admin@1.1.1.4 ")
c.timeout = 4
c.expect("password: ")
c.sendline("admin")
c.expect("# ")
c.sendline('show version ')
c.expect("# ")









    








































#def a(str):
#	for i in range(0,len(str)):
#		if str[i].isalpha():
#			if str[i-1] != '+' or str[i+1] != '+':
#				return 'false'
#	return 'True'
#
#print a("+a+b+c+")