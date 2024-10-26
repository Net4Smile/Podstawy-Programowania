def f(number1: int, number2: int, operation: str):
  result = 0
  if operation == '+':
    result = number1 + number2
  elif operation == '-':
    result = number1 - number2
  elif operation == '*':
    result = number1 * number2
  elif operation == '/':
    result = number1 / number2
  elif operation == '%':
    result = number1 % number2
  elif operation == '**':
    result = number1 ** number2
  return result

print(f(2, 3, "+"))
print(f(2, 3, "%"))
print(f(2, 3, "**"))
print(f(2, 3, "*"))
print(f(2, 3, "-"))
