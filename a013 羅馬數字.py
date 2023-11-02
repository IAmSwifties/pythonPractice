nums = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50,
        'C' : 100, 'D' : 500, 'M' : 1000}
strings = {1 : 'I',4 : 'IV', 5 : 'V',9 : 'IX', 10 : 'X',40 : 'XL', 50 : 'L',
           90 : 'XC', 100 : 'C',400 : 'CD', 500 : 'D',900 : 'CM', 1000 : 'M'}

def strToNum(k):
    num = 0
    n = k[0]
    for m in k[1:]:
        if nums[n] < nums[m]:
            num -= nums[n]
        else:
            num += nums[n]
        n = m
    num += nums[n]
    return num

def numToStr(k):
    string = ''
    keys = list(strings.keys())[::-1]
    for i in keys:
        while (k >= i):
            string = string + strings[i]
            k -= i
    return string

while True:
    try:
        string = input()
        if string == '#':
            break
        a, b = [str(s) for s in string.split()]
        num1 = strToNum(a)
        num2 = strToNum(b)
        temp = abs(num1 - num2)
        if temp == 0:
            print('ZERO')
        else:
            print(numToStr(temp))
    except:
        break
