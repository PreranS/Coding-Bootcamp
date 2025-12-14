def is_even_odd(n: int) -> str:
    return "Even" if n % 2 == 0 else "Odd"


if __name__ == "__main__":
    print(is_even_odd(10))
