def f(number: int, even: bool):
  sum = 0
  for char in str(number):
    num = int(char)
    if even:
      if num % 2 == 0:
        sum += num
    else:
      if num % 2 != 0:
        sum += num

  return sum

print(f(3124, True))
print(f(3124, False))
print(f(20576, False))
print(f(20576, True))
print(f(13115, True))