def f(a, b):
    if a * b == 0:
        return max(a, b)
    return f(b, a % b)


print(f(int(input()), int(input())))
