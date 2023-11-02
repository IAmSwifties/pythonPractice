while True:
    try:
        n, m = [int(s) for s in input().split()]
        s, k = 0, 1
        while True:
            s += n
            if s > m:
                print(k)
                break
            n += 1
            k += 1
    except:
        break
