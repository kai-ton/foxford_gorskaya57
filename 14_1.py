a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
print((a2 - a1) * 3600 + (b2 - b1) * 60 + (c2 - c1))
