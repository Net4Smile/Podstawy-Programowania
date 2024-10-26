def create_2d_array(x, y):
  array = []
  for i in range(x):
    array.append([])
    for j in range(y):
      array[i].append(0)

  return array

array = create_2d_array(3, 5)

print(array)