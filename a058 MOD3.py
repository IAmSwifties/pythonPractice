n = int(input())
a = []
k0 = 0
k1 = 0
k2 =0
for i in range(n):
    a.append(int(input()))
for i in a:
    if i % 3 == 0:
        k0 += 1
    elif i % 3 == 1:
        k1 += 1
    else:
        k2 += 1
print(k0, k1, k2)
