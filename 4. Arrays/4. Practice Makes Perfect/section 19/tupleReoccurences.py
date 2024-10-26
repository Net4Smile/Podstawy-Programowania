tuple = tuple([50, 20, 40, 50, 30, 50])

value = 50

reocurrences = 0

for i in range(len(tuple)):
  if tuple[i] == value:
    reocurrences += 1

print("Tuple:", tuple)
print("Value:", value)
print("Number of occurences:", reocurrences)
