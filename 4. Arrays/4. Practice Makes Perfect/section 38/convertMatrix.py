# Create a function that convert two-dimensional (2D) array into 1D. Then create a program that prints 1D array for the following 2D arrays.
def convert_matrix(m):
  result = []
  for i in range(len(m)):
    for j in range(len(m[0])):
      result.append(m[i][j])
  return result

matrix1 = [
  [2, 3],
  [1, 5]
]

matrix2 = [
  [5, 0, 3, 7, 5],
  [9, 0, 9, 1, 2]
]

matrix3 = [
  [2, 1],
  [3, 5],
  [7, 4],
  [2, 6]
]

convertedMatrix1 = convert_matrix(matrix1)
convertedMatrix2 = convert_matrix(matrix2)
convertedMatrix3 = convert_matrix(matrix3)

def fancy_print(matrix):
  for i in range(len(matrix)):
    print(matrix[i], end=" ")
  print()

print("Matrix 1:")
fancy_print(matrix1)

print("Converted matrix 1:")
fancy_print(convertedMatrix1)

print("\n")

print("Matrix 2:")
fancy_print(matrix2)

print("Converted matrix 2:")
fancy_print(convertedMatrix2)

print("\n")

print("Matrix 3:")
fancy_print(matrix3)

print("Converted matrix 3:")
fancy_print(convertedMatrix3)