def f(a, b):
    if b == 0:
        return a
    return f(b, a % b)


x = 0
for i in range(10000, 100000):
    if f(92, i) == 1:
        x += 1
print(x)
