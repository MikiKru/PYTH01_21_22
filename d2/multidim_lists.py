matrix = [[1, 2, 3], [3, 4, 2], [3, 2, 1]]

print(matrix)

for row in matrix:
    for col in row:
        print(col, end=" ")
    print()

print(matrix[2][0])
print(matrix[1][2])

