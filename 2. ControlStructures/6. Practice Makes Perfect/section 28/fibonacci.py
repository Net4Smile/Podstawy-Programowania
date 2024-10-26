numberOne = 0
numberTwo = 1
nextNumber = numberOne

for i in range(20):
  print(nextNumber)
  numberOne = numberTwo
  numberTwo = nextNumber
  nextNumber = numberOne + numberTwo

print()