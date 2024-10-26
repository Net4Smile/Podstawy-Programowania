polishNamesArray = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longestName = ""

for i in range(len(polishNamesArray)):
  if len(polishNamesArray[i]) > len(longestName):
    longestName = polishNamesArray[i]

print("Names:", ' '.join(polishNamesArray))
print("Longest name:", longestName)
