import math

def prime(k):
    if (k == 2 or k == 3):
        return True
    elif k >= 4:
        if (k % 6 != 1 and k % 6 != 5):
            return False
        m = math.ceil(math.sqrt(k))
        for i in range(5, m + 1, 6):
            if (k % i == 0 or k % (i + 2) == 0):
                return False
        return True
    else:
        return False

while True:
    try:
        a, b = [int(s) for s in input().split()]
        ans = 0
        for i in range(a, b + 1):
            if (prime(i)):
                ans += 1;
        print(ans)
    except:
        break
