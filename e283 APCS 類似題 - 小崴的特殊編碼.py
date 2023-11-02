import sys
dic = {'0 1 0 1':'A', '0 1 1 1':'B', '0 0 1 0':'C',
       '1 1 0 1':'D', '1 0 0 0':'E', '1 1 0 0':'F'}
for i in sys.stdin:
    n = int(i)
    for i in range(n):
        print(dic[sys.stdin.readline().rstrip()], end = '')
    print()
