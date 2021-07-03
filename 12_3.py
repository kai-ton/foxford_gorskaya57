n = int(input())
a = []
for i in range(n):
    a.append([])
    for j in range(n):
        if (i + j) % 2 == 1:
            a[i].append('*')
        else:
            a[i].append('.')
for i in range(n):
    print(*a[i], sep='')
