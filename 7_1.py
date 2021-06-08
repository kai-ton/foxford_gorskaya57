a = 0
for i in range(1000, 10000):
    if i % 10 + i // 10 % 10 + i // 100 % 10 + i // 1000 == 20:
        a += i
print(a)
