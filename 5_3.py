a = int(input())
b = int(input())
a, b = min(a, b), max(a, b)
print((b + 1) // 2, a)
