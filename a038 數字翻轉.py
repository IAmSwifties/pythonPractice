a = input()[::-1]
while a[0] == '0':
    if int(a) == 0:
        print('0')
        break
    a = a[1:]
if int(a) != 0:
    print(a)
