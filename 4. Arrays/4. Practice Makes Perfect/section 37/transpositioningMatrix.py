def transpose_matrix(m):
  result = []
  for i in range(len(m[0])):
    row = []
    for j in range(len(m)):
        row.append(m[j][i])
    result.append(row)
    
  return result

matrix1 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

matrix2 = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10]
]

matrix3 = [
  [5, 6, 7, 8]
]

transposedMatrix1 = transpose_matrix(matrix1)
transposedMatrix2 = transpose_matrix(matrix2)
transposedMatrix3 = transpose_matrix(matrix3)

def fancy_print(matrix):
  for i in range(len(matrix)):
    print(" ".join(map(str, matrix[i])))

print("Matrix 1:")
fancy_print(matrix1)

print("Transposed matrix 1:")
fancy_print(transposedMatrix1)

print("\n")

print("Matrix 2:")
fancy_print(matrix2)

print("Transposed matrix 2:")
fancy_print(transposedMatrix2)

print("\n")

print("Matrix 3:")
fancy_print(matrix3)

print("Transposed matrix 3:")
fancy_print(transposedMatrix3)