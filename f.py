
a = []
c = []

def fibonacci(n):
	for i in range(0,n+1):
		a.append(i)
	for i in range(0,len(a) - 1):
		if a[i] == 0 or a[i] == 1:
			c.append(a[i])
		elif a[i] != 0 or a[i] != 1:
			a[i] = a[i -1] + a [i - 2]
			c.append(a[i])
	print sorted(c)


fibonacci(5)

cube = list(map(lambda x:x**3 ,c))
print cube





