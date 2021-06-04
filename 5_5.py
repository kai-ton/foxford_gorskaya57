a, b, c = map(int, input().split())
if a // 2 > c - b - 1:
    print(c - b - 1)
else:
    print(b + c - a + 1)
