def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

a = int(input())
b = int(input())

print(a*b//gcd(a,b))