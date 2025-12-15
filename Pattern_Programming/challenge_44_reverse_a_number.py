num = int(input("Enter number: "))
rev = 0

temp = num
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10

print("Reverse:", rev)
