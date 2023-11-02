while True:
    try:
        a = input().lower()
        b = a[::-1]
        a1 = filter(str.isalnum, a)
        b1 = filter(str.isalnum, b)
        a2, b2 = [''.join(list(a1)), ''.join(list(b1))]
        if a2 == b2:
            print('yes !')
        else:
            print('no...')
    except:
        break
