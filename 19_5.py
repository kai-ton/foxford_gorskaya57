a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
x = 0
for i in range(len(a)):
    x += a[i] * b[i]
print(x)
