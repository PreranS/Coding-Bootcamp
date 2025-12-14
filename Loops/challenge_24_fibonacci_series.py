def fibonacci(n):
    res = []
    a, b = 1, 1
    for _ in range(n):
        res.append(a)
        a, b = b, a + b
    return res


if __name__ == "__main__":
    n=int(input("Enter the number of terms: "))
    print(fibonacci(n))
