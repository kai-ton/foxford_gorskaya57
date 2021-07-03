a = input()
b = (len(a) + 1) // 2
print(a[b:] + a[:b], sep='')
