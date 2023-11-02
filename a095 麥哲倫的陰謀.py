while True:
    try:
        a, b = [int(s) for s in input().split()]
        if (a == b):
            print(b)
        else:
            print(b + 1)
    except:
        break
