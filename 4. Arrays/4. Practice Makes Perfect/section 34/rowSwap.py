import random

array = [
  [random.randint(1, 100) for i in range(5)] for j in range(3)
]

print("Array:", array)

array[0], array[2] = array[2], array[0]

print("Array after swap:", array)