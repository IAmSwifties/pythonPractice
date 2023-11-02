word = input()
word0 = []
for i in word:
    word0.append(chr(ord(i) - 7))
print(*word0 , sep = '')
