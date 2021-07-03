n = int(input())
a = []
for i in range(n):
    a.append([])
    for j in range(n):
        if i == j or i + j == n - 1 or i == n // 2 or j == n // 2:
            a[i].append('*')
        else:
            a[i].append('.')
for i in range(n):
    print(*a[i])
