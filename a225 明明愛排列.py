while True:
    try:
        n = int(input())
        print(*sorted([int(s) for s in input().split()], key = lambda x:(x%10, -x)))
    except:
        break
