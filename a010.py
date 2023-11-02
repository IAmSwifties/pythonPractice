n = int(input())
a = []
i = 2
m = 0
while True:
    if n == 1:
        break
    elif n % i == 0:
        a.append(i)
        n = n // i
    else:
        i = i+1
        pass
for i in a:
    m = a.count(i)
    if m != 1:
        print(i , '^' , m , sep = '' , end = ' ')
        for j in range(1,m):
            a.remove(i)
    else:
        print(i , end = ' ')
    if i != a[-1]:
        print('*' , end = ' ')
