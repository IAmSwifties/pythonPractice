t = int(input())
for i in range(t):
    tmp = input()
    A = tmp.strip()
    a = [int(s) for s in A.split()]
    if a[1] - a[0] == a[2] - a[1]:
        a.append(a[3] + (a[1] - a[0]))
    else:
        a.append(a[3] * (a[1] // a[0]))
    print(' '.join([str(i) for i in a]))
