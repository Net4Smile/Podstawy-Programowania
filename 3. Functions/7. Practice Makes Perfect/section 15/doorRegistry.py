def f(detector: str):
  sameCharacterCount = 0

  for char in detector:
    if sameCharacterCount == 3:
      return True

    if char == "+":
      sameCharacterCount += 1
    elif char == "-":
      sameCharacterCount -= 1
      
  return False

print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))