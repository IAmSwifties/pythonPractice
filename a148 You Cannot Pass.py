while True:
    try:
        a = [int(s) for s in input().split()]
        x = sum(a[1:])
        x = x // a[0]
        if x > 59:
            print('no')
        else:
            print('yes')
    except:
        break
