def brackets(ans, temp, n, left, right):
    if (len(temp) == 2 * n):
        ans.append(temp)
        return
    if (left < n):
        temp = temp + '('
        brackets(ans, temp, n, left + 1, right)
        temp = temp[:-1]
    if (right < left):
        temp = temp + ')'
        brackets(ans, temp, n, left, right + 1)
        temp = temp[:-1]

while True:
    try:
        n = int(input())
        ans = []
        temp = ''
        brackets(ans, temp, n, 0, 0)
        for i in ans:
            print(i)
        print()
    except:
        break
