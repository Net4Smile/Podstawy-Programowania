def f(password: str):
  if len(password) >= 6:
    characters = {}
    for char in password:
      characters[char] = password.count(char)
      if characters[char] > 1:
        return False
    return True
  return False

print(f("ax15"))
print(f("book123"))
print(f("A2water3"))
print(f("qwerty"))
print(f(""))