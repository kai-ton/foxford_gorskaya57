b = 'abcdefghijklmnopqrstuvwxyz'.upper()
a = b[:int(input())]
z = ''
if len(a) % 2 == 1:
    for i in range(len(a) // 2):
        z = a[i] + z
        z = a[-1 - i] + z
    z = a[len(a) // 2] + z
else:
    for i in range(len(a) // 2):
        z = a[-1 - i] + z
        z = a[i] + z
print(z)
