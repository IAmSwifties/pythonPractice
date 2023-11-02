n = int(input())
for i in range(n):
    a = input()
    s = 1
    for j in range(len(a)):
        s *= int(a[j])
    print(s)
