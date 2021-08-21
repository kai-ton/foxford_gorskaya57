n = 10 ** 5
a = list(i for i in range(n + 1))
a[0], a[1] = 0, 0
for i in range(2, n - 1):
    if a[i] != 0:
        for j in range(a[i] * 2, n + 1, a[i]):
            a[j] = 0
for i in range(n, -1, -1):
    print(a[i])
    if a[i] != 0 and str(a[i])[::-1] == str(a[i]):
        print(a[i])
        break
