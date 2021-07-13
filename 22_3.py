n = int(input())
x = list(map(int, input().split()))
a = 1
for i in range(1, n):
    if x[i] > x[i - 1]:
        a += 1
print(a)
