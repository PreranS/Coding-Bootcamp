# SkillAssure HandsOn Framework - SAHF
# 2D Arrays & Matrix Operations (Challenges 55–60)

# Accept matrix dimensions
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Coding Challenge 55: Create & display 2D array row-wise
matrix = []
print("\nEnter matrix elements:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Element [{i}][{j}]: ")))
    matrix.append(row)

print("\nMatrix (Row-wise):")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()

# Coding Challenge 56: Sum of all elements
total = 0
for i in range(rows):
    for j in range(cols):
        total += matrix[i][j]
print("Sum of all elements:", total)

# Coding Challenge 57: Search element in 2D array
search = int(input("Enter element to search: "))
found = False

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == search:
            found = True
            pos_row, pos_col = i, j
            break
    if found:
        break

if found:
    print(f"Element found at position [{pos_row}][{pos_col}]")
else:
    print("Element not found")

# Coding Challenge 58 & 59: Display transpose of matrix
print("\nTranspose of the matrix:")
for j in range(cols):
    for i in range(rows):
        print(matrix[i][j], end=" ")
    print()

# Coding Challenge 60: Matrix Multiplication
print("\nEnter second matrix for multiplication:")
rows2 = int(input("Enter number of rows: "))
cols2 = int(input("Enter number of columns: "))

if cols != rows2:
    print("Matrix multiplication not possible")
else:
    matrix2 = []
    for i in range(rows2):
        row = []
        for j in range(cols2):
            row.append(int(input(f"Element [{i}][{j}]: ")))
        matrix2.append(row)

    result = []
    for i in range(rows):
        res_row = []
        for j in range(cols2):
            sum = 0
            for k in range(cols):
                sum += matrix[i][k] * matrix2[k][j]
            res_row.append(sum)
        result.append(res_row)

    print("\nResultant Matrix:")
    for i in range(rows):
        for j in range(cols2):
            print(result[i][j], end=" ")
        print()
