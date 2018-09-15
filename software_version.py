import re
b = open('test.txt', "r")
d = []
#c = []
for i in b:
	c =  i.split()
	#print c[0],c[4],c[6],c[7]
	d.append(c[8])
for j in d:
	if j != '200':
		print c[0],c[3],c[4],c[6],c[7]
	#c = re.compile(r'\d+\.\d+\.\d+\.\d+\ \-*\ \-*\ \[\d+')
	#d = re.match(c,i)
	#print d.group()



















#class x():
#	def __init__(self,l):
#		self.l = l
#	def check(self):
#		d = []
#		if self.l >16:
#			d.append(self.l)
#			return d

#c = x(20)
#print c.check()



















#class Triangle():
#	def __init__(self,angle1,angle2,angle3):
#		self.angle1 = angle1
#		self.angle2	= angle2
#		self.angle3	= angle3
#	number_of_sides = 3
#	def check_angles(self):
#		if self.angle1 + self.angle2 + self.angle3 == 180:
#			return True
#		else:
#			return False

#my_triangle = Triangle(90,30,60)
#print my_triangle.check_angles()
#print my_triangle.number_of_sides








#class bank:
#	def __init__(self,name,balance):
#		self.name = name
#		self.balance = balance
#	def withdraw(self,amount):
#		if amount > self.balance:
#			print "fail"
#		else:
#			self.balance = self.balance - amount
#			self.balance = balance
#			return self.balance
#	def deposit(self,amount):
#		if amount > 0:
#			self.balance = self.balance + amount
#			return self.balance

	

#d = bank('Deepesh',100)
#print d.withdraw(50)

