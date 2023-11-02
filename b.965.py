while True:
    r , c , m = [int(s) for s in input().split()]
    a = []
    b = []
    p = []
    q = []
    for i in range(r):
        b = [int(s) for s in input().split()]
        a.append(b)
        b.clear
    k = [int(t) for t in input().split()]
    k = k[::-1]
    for j in k:
        if j == 0:
            for y in range(c-1 , -1 , -1):
                for x in range(r):
                    p.append(a[x][y])
                print(p)
                q.append(p)
                print(q)
                p.clear()
                print(q)
            
        else:
            pass
            #a = a[::-1]
    #print(*a)
                    
