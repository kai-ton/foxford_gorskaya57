def v(a):
    b = 0
    for j in range(len(a)):
        for i in range(2, int(a[j]**0.5) + 1):
            if a[j] % i == 0:
                break
        else:
            print(a[j])
            b += 1
    print(b)

v([2445304333, 4092947611, 6278397751, 6300693019, 7999219357])
