def star(n: int):
  return "*" * n

array = [2, 6, 4, 9, 7]

for i in range(len(array)):
  print(str(array[i]) + ": " + star(array[i]))