def bubblesort(array):
  n = len(array)
  for i in range(n):
    for j in range(0, n - i - 1):
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]

  return array

array = [5, 3, 8, 4, 2, 1]
array2 = [1, 6, 3, 2, 5, 8]
array3 = [1, 4, 3, 4, 1, 8, 9]

print(bubblesort(array))
print(bubblesort(array2))
print(bubblesort(array3))