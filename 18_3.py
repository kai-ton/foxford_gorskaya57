a = list(map(int, input().split()))
b = 99999999999
for i in range(len(a)):
    if 0 < a[i] < b:
        b = a[i]
print(b)
