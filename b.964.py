n = int(input())
a = [int(s) for s in input().split()]
good = 101
bad = -1
for j in a:
    if j >= 60 and j < good:
        good = j
    elif j < 60 and j > bad:
        bad = j
    else:
        pass
a.sort()
print(*a)
if bad == -1:
    print('best case')
else:
    print(bad)
if good == 101:
    print('worst case')
else:
    print(good)
