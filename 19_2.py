a = int(input())
b = 0
for i in 10, 5, 2, 1:
    b += a // i
    a %= i
print(b)
