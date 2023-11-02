n = int(input())
a, x, ans = [], [], []
j, k, s = 1, 1, 0
for i in range(n):
    a = int(input())
    b = int(input())
    k, s = 1, 0
    while True:
        if k**2 >= a and k**2 <= b:
            s += k**2
        if k**2 > b:
            break
        k += 1
    ans.append(s)
for i in ans:
    print('Case %s:'%j, i)
    j += 1
