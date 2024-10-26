def f(number1: int, number2: int, number3: int):
  numberList = [number1, number2, number3].sort()
  return numberList[-1] - numberList[0]

print(f(7, 4, 9))
print(f(2, 12, 8))