def student_report_card(name: str, s1: float, s2: float, s3: float) -> dict:
    total = s1 + s2 + s3
    avg = total / 3
    if avg >= 60:
        grade = "1st Class"
    elif avg >= 50:
        grade = "2nd Class"
    elif avg >= 35:
        grade = "Pass"
    else:
        grade = "Fail"
    return {"name": name, "total": total, "average": avg, "class": grade}


if __name__ == "__main__":
    print(student_report_card("Asha", 70, 65, 80))
