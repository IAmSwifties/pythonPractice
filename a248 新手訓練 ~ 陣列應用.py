while True:
    try:
        a, b, n = [int(s) for s in input().split()]
        a *= (10 ** n)
        a //= b
        ans = str(a)
        ans1 = ans[:-n]
        ans2 = ans[-n:]
        if ans1 == '':
            ans1 = '0'
        if (len(ans2) < n):
            for i in range(n - len(ans2)):
                ans2 = '0' + ans2
        print(ans1 , '.', ans2, sep = '')
    except:
        break
