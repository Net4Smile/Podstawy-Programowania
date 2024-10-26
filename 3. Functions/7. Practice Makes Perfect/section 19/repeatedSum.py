def f(number: int):
  sum = 0
  numberDigits = {}
  
  for char in str(number):
    if char in numberDigits:
      numberDigits[char] += 1
    else:
      numberDigits[char] = 1

  for key, value in numberDigits.items():
    if value > 1:
      sum += int(key) * value

  return sum

print(f(1027))
print(f(230335))
print(f(513553007))
