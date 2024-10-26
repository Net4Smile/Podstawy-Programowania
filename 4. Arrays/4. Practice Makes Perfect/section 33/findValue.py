array = [
  [-38, 19], 
  [5,   40], 
  [-7,  11], 
  [29,  16]
]

# Create a program that finds the smallest and largest values in the array and in which row and column they are located.

minValue = 0
maxValue = 0

for i in range(1, len(array) + 1):
  for j in range(1, len(array[i - 1]) + 1):
    if array[i - 1][j - 1] < minValue:
      minValue = array[i - 1][j - 1]
      minRow = i
      minCol = j
      continue
    if array[i - 1][j - 1] > maxValue:
      maxValue = array[i - 1][j - 1]
      maxRow = i
      maxCol = j
      continue
    if array[i - 1][j - 1] == minValue:
      minRow = i
      minCol = j
      continue
    if array[i - 1][j - 1] == maxValue:
      maxRow = i
      maxCol = j
      continue

print("Smallest value:", minValue)
print("Largest value:", maxValue)
print("Min is in row:", minRow)
print("Min is in column:", minCol)
print("Max is in row:", maxRow)
print("Max is in column:", maxCol)