
a = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
for i in dragonLoot:
	for j in a.keys():
		if i == j:
			a[j] = a[j] + 1
print a 

			



