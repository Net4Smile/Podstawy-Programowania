array = [15, 8, 31, 47, 2, 19]

arithmeticMean = 0

i = 0

while i < len(array):
  arithmeticMean += array[i]
  i += 1
  arithmeticMean /= len(array)

print("Arithmetic mean:", arithmeticMean)