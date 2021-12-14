dim = 4

matrix = [[1 if c_index == r_index else 0 for c_index in range(dim)] for r_index in range(dim)]

# for r_index in range(dim):
#     matrix.append([])
#     for c_index in range(dim):
#        matrix[r_index].append(1 if c_index == r_index else 0)
print(matrix)

