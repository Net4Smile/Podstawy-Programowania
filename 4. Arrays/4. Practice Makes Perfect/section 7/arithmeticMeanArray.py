array = [15, 8, 31, 47, 2, 19]

arithmeticMean = 0

for i in range(len(array)):
  arithmeticMean += array[i]
  arithmeticMean /= len(array)

print("Arithmetic mean:", arithmeticMean)