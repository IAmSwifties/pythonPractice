alpha = { 'A' : 10 , 'B' : 11 , 'C' : 12 , 'D' : 13 , 'E' : 14 ,
          'F' : 15 , 'G' : 16 , 'H' : 17 , 'I' : 34 , 'J' : 18 ,
          'K' : 19 , 'L' : 20 , 'M' : 21 , 'N' : 22 , 'O' : 35 ,
          'P' : 23 , 'Q' : 24 , 'R' : 25 , 'S' : 26 , 'T' : 27 ,
          'U' : 28 , 'V' : 29 , 'W' : 32 , 'X' : 30 , 'Y' : 31 ,
          'Z' : 33}
in1 = input()
s = 0
for i in range(len(in1)):
    j = 8 - i
    s += int(in1[i]) * j
s += int(in1[-1])
for i in alpha:
    a = alpha[i]//10 + alpha[i]%10*9
    if ((a+s) % 10) % 10 == 0:
        print(i, end = '')
