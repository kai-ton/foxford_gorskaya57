a = list(map(int, input()))
b = []
for i in range(len(a)):
    if a[i] % 2 == 0:
        b.append(a[i])
if b != []:
    print(min(b))
else:
    print('NO')
