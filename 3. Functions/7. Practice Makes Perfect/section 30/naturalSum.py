def sum_natural(n: int):
  if n <= 1:
    return n
  
  return n + sum_natural(n - 1)

print(sum_natural(10))