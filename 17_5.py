def f(a):
    if len(a) == 1:
        return a[0]
    if len(a) == 2:
        if a[1] == 0:
            return a[0]
        return f([a[1], a[0] % a[1]])
    return f([a[0], f(a[1::])])

int(input())
print(f(list(map(int, input().split()))))
