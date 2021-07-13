from copy import deepcopy

q, t = map(int, input().split())
x = [[0] * (q + 2)] \
    + [[0] + list(map(int, input().split())) + [0] for j in range(q)] \
    + [[0] * (q + 2)]
for _ in range(t):
    z = deepcopy(x)
    for i in range(1, q + 1):
        for j in range(1, q + 1):
            a = z[i - 1][j - 1] + z[i - 1][j] + z[i - 1][j + 1] + z[i + 1][j - 1] + z[i + 1][j] + z[i + 1][j + 1] + z[i][j - 1] + z[i][j + 1]
            if z[i][j] == 0 and a == 3:
                x[i][j] = 1
            elif 2 != a != 3:
                x[i][j] = 0
[print(*i[1:-1]) for i in x[1:-1]]
