def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
x , y = [int(s) for s in input().split()]
print(gcd(x,y))
