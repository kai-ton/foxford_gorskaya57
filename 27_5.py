a = int(input())
b = list(map(int, input().split()))
for i in range(2, a):
    if b[i - 2] < b[i - 1]:
        b[i] += b[i - 2]
    else:
        b[i] += b[i - 1]
print(b[-1])
