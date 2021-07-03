n = int(input())
a = []
for i in range(n):
    a.append([])
    for j in range(n * 2 - 1):
        if (n - i - 1) <= j <= (n + i - 1):
            a[i].append('*')
        else:
            a[i].append(' ')
for i in range(n):
    print(*a[i], sep='')
