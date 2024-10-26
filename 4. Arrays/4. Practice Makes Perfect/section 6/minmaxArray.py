array = [-15, 8, -31, 47, -2, 19]

minValue = 0
maxValue = 0

for i in range(len(array)):
  if array[i] < minValue:
    minValue = array[i]
  if array[i] > maxValue:
    maxValue = array[i]

print("Min:", minValue)
print("Max:", maxValue)