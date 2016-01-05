a = int(input())
b = int(input())
c = int(input())
d = int(input())

print('\t',end='')
for i in range(c,d+1):
	if i<d:
		print(i,end='\t')
	else:
		print(i)

for i in range(a, b+1):
	print(i,end='\t')
	for j in range(c, d+1):
		if j<d:
			print(i*j,end='\t')
		else:
			print(i*j,end='')
	print()

