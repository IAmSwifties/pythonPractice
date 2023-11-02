alpha = { 'A' : 10 , 'B' : 11 , 'C' : 12 , 'D' : 13 , 'E' : 14 ,
          'F' : 15 , 'G' : 16 , 'H' : 17 , 'I' : 34 , 'J' : 18 ,
          'K' : 19 , 'L' : 20 , 'M' : 21 , 'N' : 22 , 'O' : 35 ,
          'P' : 23 , 'Q' : 24 , 'R' : 25 , 'S' : 26 , 'T' : 27 ,
          'U' : 28 , 'V' : 29 , 'W' : 32 , 'X' : 30 , 'Y' : 31 ,
          'Z' : 33}
id1 = input()
num = alpha[id1[0]]
id2 = id1[1:]
id3 = int(id2[-1])
num = num % 10 * 9 + num // 10
num2 = 0
for i in range(len(id2)):
    j = 8 - i
    num2 += int(id2[i]) * j
sum = num + num2 + id3
if sum % 10 == 0:
    print('real')
else:
    print('fake')
