n = int(input("Enter N: "))
num = 1

for i in range(1, n+1):
    for j in range(i):
        square = num * num
        if num % 2 == 0:
            square = -square
        print(square, end=" ")
        num += 1
    print()
