def f(a, b):
    if b == 0:
        return a
    else:
        return f(a + 1, b - 1)


print(f(int(input()), int(input())))
