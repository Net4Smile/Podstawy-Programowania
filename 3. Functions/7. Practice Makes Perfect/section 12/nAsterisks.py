def f(n: int):
  asterisks = ''
  for i in range(n):
    if i == n - 1:
      asterisks += '*'
    else:
      asterisks += '*/'
  return asterisks

print(f(4))
print(f(1))