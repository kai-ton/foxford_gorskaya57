def f(a, b):
    if b == 0:
        return a
    return f(b, a % b)


print(f(int(input()), int(input())))
