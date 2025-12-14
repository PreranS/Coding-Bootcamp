def salary_tax_check(name: str, salary: float) -> str:
    return f"{name} must pay tax." if salary > 300000 else f"{name} need not pay tax."


if __name__ == "__main__":
    print(salary_tax_check("Ravi", 250000))
