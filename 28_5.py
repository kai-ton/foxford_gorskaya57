y, x = map(int, input().split())
a = list(list(map(int, input().split())) for i in range(y))
for i in range(y):
    for j in range(x):
        if a[i][j] != 0:
            if j != 0 != i and a[i - 1][j] == 0 == a[i][j - 1]:
                a[i][j] = 0
            elif j == 0 != i:
                a[i][j] = a[i - 1][j]
            elif j != 0 == i:
                a[i][j] = a[i][j - 1]
            elif j != 0 != i:
                a[i][j] = a[i - 1][j] + a[i][j - 1]
print(a[y - 1][x - 1])
