from math import *
while True:
    try:
        x = int(input())
        i, s= 2, 0
        while x != 1:
            if i == sqrt(x) and x % i != 0:
                s = x
                break
            while x % i == 0:
                x //= i
                s += i
            i += 1
        print(s)
    except:
        break
