def seq(n):
    res = []
    val = 1
    diff = 1
    for _ in range(n):
        res.append(val)
        diff += 1
        val += diff
    return res


if __name__ == "__main__":
    n=int(input("Enter the number of terms: "))
    print(seq(n))
