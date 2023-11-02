while True:
    try:
        n = int(input())
        if n == 0:
            break
        for i in range(n):
            if i % 7 != 0:
                print(i, end = ' ')
        print('')
    except:
        break
