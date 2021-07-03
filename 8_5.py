a = int(input())
b = 1
while a >= b:
    if b == a:
        print('YES')
        break
    b *= 2
else:
    print('NO')
