while True:
    try:
        n = int(input())
        print(*sorted([int(s) for s in input().split()]), sep = ' ')
    except:
        break
