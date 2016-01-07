s = input()
c = s[0]
sn = ''
j = 0
i = 0
while i < len(s):
	c = s[i]
	while i<len(s) and s[i] == c:
		j+=1
		i+=1
	if j>0:
		sn =sn+c+str(j)
	j=0
print(sn)
