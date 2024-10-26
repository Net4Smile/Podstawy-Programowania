def calculate(string: str, letterToCheck: str):
  count = 0
  for char in string:
    if char == letterToCheck:
      count += 1
  return count