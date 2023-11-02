n, m = [int(s) for s in input().split()]
a, ans = [], []
s = 0
for i in range(n, m+1):
    a = []
    for j in range(len(str(i))):
        a.append(int(str(i)[j]))
    s = sum(k**len(str(i)) for k in a)
    if s == i:
        ans.append(s)
if ans == []:
    print('none')
else:
    print(*ans, sep = ' ')
