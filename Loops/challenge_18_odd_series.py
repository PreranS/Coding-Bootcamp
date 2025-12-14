def odd_series(n):
    return [i for i in range(1, n + 1) if i % 2 == 1]


if __name__ == "__main__":
    n=int(input("Enter the number of terms: "))
    print(odd_series(n))
