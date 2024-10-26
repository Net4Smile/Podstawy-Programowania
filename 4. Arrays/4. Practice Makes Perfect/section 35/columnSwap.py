import random

array = [
  [random.randint(1, 100) for i in range(5)] for j in range(3)
]

print("Array:")

for i in range(len(array)):
  print(" ".join(map(str, array[i])))

for i in range(len(array)):
  array[i][0], array[i][len(array) + 1] = array[i][len(array) + 1], array[i][0]

print("Array after swap:")
for i in range(len(array)):
  print(" ".join(map(str, array[i])))
