array = [34, 7, 19, 4, 21, 8]

i = 0

while True:
  if i == len(array):
    break

  if array[i] % 2 == 0:
    print(array[i])
  i += 1