n = int(input("Enter N: "))
num = 1

for i in range(n):
    if i % 2 == 0:
        print(num, end=" ")
    else:
        print(-num, end=" ")
    num += 4
