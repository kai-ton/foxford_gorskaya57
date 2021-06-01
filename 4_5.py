c = int(input())
d = int(input())
a = c // 10 + c % 10
b = d // 10 + d % 10
if a > b:
    print(c)
elif b > a:
    print(d)
elif c > d:
    print(c)
else:
    print(d)
