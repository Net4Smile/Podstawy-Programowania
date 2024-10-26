def f(n: int):
  numberOne = 0
  numberTwo = 1
  nextNumber = numberOne + numberTwo

  for i in range(n - 3):
    numberOne = numberTwo
    numberTwo = nextNumber
    nextNumber = numberOne + numberTwo
  
  return nextNumber

    
print(f(5))
print(f(9))