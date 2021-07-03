a = 'abcdefghijklmnopqrstuvwxyz'
z = 'zyxwvutsrqponmlkjihgfedcba'
x = list(input())
for i in range(len(x)):
    x[i] = z[a.find(x[i])]
print(*x, sep='')
