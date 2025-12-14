def squares_series(n):
    return [i * i for i in range(2, n + 1)]


if __name__ == "__main__":
    n= int(input("Enter the number of terms: "))
    print(squares_series(n))
