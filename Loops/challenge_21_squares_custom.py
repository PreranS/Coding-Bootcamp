def series_custom(n):
    res = []
    for i in range(1, n + 1):
        res.append(i * i)
    return res


if __name__ == "__main__":
    n=int(input("Enter the number of terms: "))
    print(series_custom(n))
