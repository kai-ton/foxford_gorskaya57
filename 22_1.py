n = int(input())
p = 0
a = 0
while n != 0:
    if n < p:
        a += 1
    p = n
    n = int(input())
print(a)
