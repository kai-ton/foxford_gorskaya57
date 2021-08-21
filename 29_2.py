n = int(input())
a = list(2 for i in range(n + 1001))
for i in range(n + 1):
    if a[i] == 2:
        a[i + 1], a[i + 2], a[i + 1000] = 1, 1, 1
print(a[n])
