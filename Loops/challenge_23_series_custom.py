def series(n):
    res = []
    val = 1
    add = 4
    for i in range(n):
        res.append(val)
        if (i+1) % 4 == 0:
            add = 8
        else:
            add = 4
        val += add
    return res


if __name__ == "__main__":
    n=int(input("Enter the number of terms: "))
    print(series(n))
