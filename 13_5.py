n = int(input())
a = []
for i in range(n):
    x = list(map(int, input().split()))
    a += [x]
for i in range(n):
    print(*a[i])
