a = 7
b = 13
c = 21
x = 10**20
ans = min(a, b, c)
f = ans * 2
left = 10**20
right = 10**22
while left + 1 < right:
    t = f + (left + right) // 2
    if t // a + (t + ans) // b + t // c < x:
        left = t - f
    else:
        right = t - f
print(right)
