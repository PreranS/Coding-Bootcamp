def series(n):
    res = []
    val = 1
    step = 3
    for _ in range(n):
        res.append(val)
        val += step
        step += 1
    return res


if __name__ == "__main__":
    n=int(input("Enter the number of terms: "))
    print(series(n))
