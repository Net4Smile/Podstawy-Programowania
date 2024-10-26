def f(product_code: str):
  sum = 0
  for i in range(len(product_code)):
    if (i != len(product_code) - 1):
      sum += int(product_code[i])
    else:
      if (sum % 7) == int(product_code[i]):
        return True
      else:
        return False

print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))