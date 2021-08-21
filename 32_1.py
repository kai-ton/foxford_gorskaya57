a, b, c, d = map(int, input().split())
print(min(min(a, b) - c, c, max(a, b) - d, d))
