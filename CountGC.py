s = input()
ss = s.upper()
a = ss.count('G')
a = a + ss.count('C')
print(100*a/len(s))