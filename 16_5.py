def f(a):
    x = int(input())
    if x == 0:
        return a
    else:
        return f(a + x)


print(f(0))
