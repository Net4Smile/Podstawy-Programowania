array = [
  [1, 2, 3, 4],
  [5, 6, 7, 8]
  ]

for i in range(len(array)):
  for j in range(len(array[i])):
    print(array[i][j], end=' ')
    
    if j == len(array[i]) - 1:
      print()