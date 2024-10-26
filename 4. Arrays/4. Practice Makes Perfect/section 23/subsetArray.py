array1 = [1, 2, 3, 4, 5]
array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Array1:", array1)
print("Array2:", array2)

for i in range(len(array1)):
  if array1[i] not in array2:
    print("Array is not a subset")
    break
  else:
    print("Array is a subset")
    break