def f(string: str):
  newString = ''
  for char in string:
    if char == string[-1:]:
      newString += char
    else:
      newString += char + '-'

  return newString


print(f("University"))
print(f("UE"))
print(f("x"))
print(f(""))