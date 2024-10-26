def f(n: int):
  string = ""
  for i in range(1, n + 1):
    string += f"{i}"
  return string

print(f(11))
print(f(4))