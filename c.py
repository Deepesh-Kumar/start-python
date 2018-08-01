n = int(raw_input(("Enter Number of Students")))
a = []
for i in range(0,n):
	 b = raw_input(("enter student name"))
	 c = float(raw_input(("Enter Marks")))
	 e = [b,float(c)]
	 a.append(e)
e = []
for i in a:
	print i[0],i[1]
	e.append(i[1])
f = min(e)
print f







