def occurs(number, array):
  if number in array:
    return True
  
  return False

array = [15, 38, 7, 23, 14]

print("Number: 23")
print("Array: " + ' '.join(map(str, array)))
print("Result: " + "number 23 appears in the array" if occurs(23, array) else "number 23 does not appear in the array")