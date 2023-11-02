while True:
    try:
        a = input().strip().lower()
        if a == '':
            print('yes !')
            continue
        a1 = filter(str.isalnum, a)
        dic = dict()
        count = 0
        for i in a1:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for j in dic:
            if dic[j] % 2 == 1:
                count += 1
        if count <= 1:
            print('yes !')
        else:
            print('no...')
    except:
        break
