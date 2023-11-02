a , b , c = map(int , input().split())
d = b ** 2 - 4 * a * c
if d == 0:
    x=int(-b / (2 * a))
    print('Two same roots x=%d'%(x))
elif d > 0:
    x1 = int((-b + d ** 0.5) / (2 * a))
    x2 = int((-b - d ** 0.5) / (2 * a))
    print('Two different roots x1=%d , x2=%d'%(x1,x2))
else:
    print('No real root')
