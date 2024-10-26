def f(binary_number: str):
  for char in binary_number:
    if char not in '01':
      return False
  return True
   
print(f("101101"))
print(f("1311a10100"))