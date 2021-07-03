a = 'abcdefghijklmnopqrstuvwxyz'
x = list(input())
b = ''
for i in range(1, 26):
    for j in range(len(x)):
        b += a[(i + a.find(x[j]) + 1) % 26]
    print(b)
    b = ''
