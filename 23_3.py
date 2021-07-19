a = list(map(int, input()))
b = 0
for i in range(len(a)):
    if a[i] % 2 == 0:
        b += a[i]
print(b)
