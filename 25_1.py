n = int(input())
a = int(input())
b = int(input())
ans, i = 0, 0
while ans < n:
    i += 1
    ans = (i//a) * (i//b)
print(i)
