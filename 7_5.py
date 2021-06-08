a = b = c = 0
for i in range(int(input())):
    x = int(input())
    if x == 0:
        a += 1
    elif x > 0:
        b += 1
    else:
        c += 1
print(a, b, c)
