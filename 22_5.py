a = list(map(int, input().split()))
n = int(input())
if n > a[0]:
    print(1)
else:
    for i in range(len(a) - 1):
        if a[i] >= n > a[i + 1]:
            print(i + 2)
            break
    else:
        print(len(a) + 1)
