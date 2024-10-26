row = []
toAdd = 1

for i in range(1, 8):
  for j in range(1, 8):
    row.append(toAdd)
    toAdd += 7
  print(" ".join(map(str, row)))
  row = []
  toAdd = i + 1