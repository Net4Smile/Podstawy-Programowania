def power(x: int, n: int):
  if n == 0:
    return 1
  elif x == 0 and n > 0:
    return 0
  else:
    return x * power(x, n - 1)
  
print(power(5, 3))