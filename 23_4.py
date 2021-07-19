a = list(map(int, input()))
for i in range(len(a) - 1):
    if a[i] == a[i + 1]:
        print('YES')
        break
else:
    print('NO')
