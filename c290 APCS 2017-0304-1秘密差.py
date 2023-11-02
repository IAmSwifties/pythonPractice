a =input()
a = a[::-1]
num = []
even = 0
odd = 0
for i in range(len(a)):
    num.append(int(a[i]))
for i in range(len(num)):
    if i % 2 == 0:
        even += num[i]
    else:
        odd += num[i]
print(abs(even - odd))
