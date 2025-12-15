n = int(input("Enter N: "))
fact = 1
num = 1

for i in range(1, n+1):
    for j in range(i):
        fact *= num
        print(fact, end=" ")
        num += 1
    print()
