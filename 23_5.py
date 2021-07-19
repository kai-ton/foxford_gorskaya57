a = int(input())
for i in range(1, 100000):
    if i // 2 // 3 // 4 == a:
        print(i, end=' ')
