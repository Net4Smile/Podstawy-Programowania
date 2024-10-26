array = [2, 3, 2, 5, 8, 1, 9, 8]

elements = {}

for i in array:
  elements[i] = array.count(i)

uniqueElements = []

for key, value in elements.items():
  if value == 1:
    uniqueElements.append(key)

print(' '.join(map(str, uniqueElements)))