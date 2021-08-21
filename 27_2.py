num = int(input())
F = [0] * num
F[0], F[1], F[2] = 1, 1, 2
for i in range(3, num):
    F[i] = F[i - 1] + F[i - 2] + F[i - 3]
print(F[num - 1])
