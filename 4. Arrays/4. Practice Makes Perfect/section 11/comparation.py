def compare(array1, array2):
  if len(array1) != len(array2):
    return False
  
  for i in range(len(array1)):
    if array1[i] != array2[i]:
      return False

  return True

array1 = ["water", "book", "sky"]
array2 = ["water", "book", "sky"]

array3 = [True, False]
array4 = [True, False, True]

array5 = [5, 3, 1]
array6 = [5, 3, 1]

array7 = [3, 2, 1]
array8 = [3, 2]

print("Array1:", array1)
print("Array2:", array2)
print("Comparison:", "arrays are the same" if compare(array1, array2) else "arrays are different")

print("Array3:", array3)
print("Array4:", array4)
print("Comparison:", "arrays are the same" if compare(array3, array4) else "arrays are different")

print("Array5:", array5)
print("Array6:", array6)
print("Comparison:", "arrays are the same" if compare(array5, array6) else "arrays are different")

print("Array7:", array7)
print("Array8:", array8)
print("Comparison:", "arrays are the same" if compare(array7, array8) else "arrays are different")