a = list(input())
x = int(input())
for i in range(len(a)):
    if 'A' <= a[i] <= 'Z':
        if ord(a[i]) - x < 65:
            print(chr(ord(a[i]) - x + 26), end='')
        else:
            print(chr(ord(a[i]) - x), end='')
    elif 'a' <= a[i] <= 'z':
        if ord(a[i]) - x < 97:
            print(chr(ord(a[i]) - x + 26), end='')
        else:
            print(chr(ord(a[i]) - x))
