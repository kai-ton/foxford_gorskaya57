a = 'aeyiuo'
c = 'qwrtpsdfghjklzxcvbnm'
b = 0
d = 0
e = 0
for i in input():
    if i in a:
        d += 1
        e = 0
    elif i in c:
        d = 0
        e += 1
    if d == 3:
        b += 1
        d = 1
    elif e == 3:
        b += 1
        e = 1
print(b)
