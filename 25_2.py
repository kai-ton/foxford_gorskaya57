w, h, n = map(int, input().split())
left = 1
right = n * w
while left + 1 < right:
    d = (left + right) // 2
    if (d // h)*(d // w) < n:
        left = d
    else:
        right = d
print(right)
