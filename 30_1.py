a = 'qwertyuiopasdfghjklzxcvbnm'
A = 'QWERTYUIOPASDFGHJKLZXCVBNM'
x = '0123456789'
b, c, d = 0, 0, 0
z = input()
if len(z) >= 8:
    for i in z:
        if i in a:
            b = 1
        elif i in A:
            c = 1
        elif i in x:
            d = 1
        if b == 1 and c == 1 and d == 1:
            print('YES')
            break
    else:
        print('NO')
else:
    print('NO')
