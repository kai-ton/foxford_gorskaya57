a = list(input())
b = 0
for i in range(len(a)):
    if int(a[i]) % 2 == 0:
        b += 1
print(b)
