a = int(input())
b = int(input())
c = int(input())
d = int(input())
a, b, c, d = min(a, b), max(a, b), min(c, d), max(c, d)
if min(b, d) - max(a, c) + 1 > 0:
    print(min(b, d) - max(a, c) + 1)
else:
    print(0)
