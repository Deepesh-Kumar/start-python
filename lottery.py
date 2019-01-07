import random

def get_numbers():
	n = raw_input("Enter the numbers: ")
	m = n.split(",")
	m = {int(i) for i in m}
	return m


def random_numbers():
	new_set = set()
	while len(new_set) < 6:
		new_set.add(random.randint(1,20))
	return new_set


def winnings():
	a = get_numbers()
	b = random_numbers()
	c = a.intersection(b)
	if c is None:
		print 'No Match'
	else:
		print 'You won %s', %(100 ** len(c))
		


winnings()
