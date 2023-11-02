while True:
    try:
        a = input()
        asc = []
        ans = []
        for i in range(len(a)):
            asc.append(ord(a[i]))
        for i in range(len(asc)-1):
            ans.append(abs(asc[i] - asc[i+1]))
        print(*ans, sep = '')
    except:
        break
