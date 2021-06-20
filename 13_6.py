q = 0
z = 0
n = int(input())
a = []
for i in range(n):
    x = list(map(int, input().split()))
    a += [x]
for i in range(n):
    q += a[i][i]
for i in range(n):
    z += a[i][n - i - 1]
if q > z:
    print(1)
elif q < z:
    print(2)
else:
    print(0)
