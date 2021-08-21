a = input().split('.')
for i in range(len(a)):
    if a[i] != '':
        if 255 < int(a[i]):
            print(0)
            break
    else:
        print(0)
        break
else:
    print(1)
