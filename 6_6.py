a = int(input())
b = int(input())
for i in range((a + 1) // 2 * 2, (b + 2) // 2 * 2, 2):
    print(i, end=" ")
