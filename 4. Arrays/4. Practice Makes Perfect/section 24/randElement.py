import random

def rand_elem(array):
  return array[random.randint(0, len(array) - 1)]

array = [15, 38, 7, 23, 14]

print("Array:", array)
print("Random element:", rand_elem(array))
print("Random element:", rand_elem(array))