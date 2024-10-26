array = [15, 38, 7, 23, 14]

chosenNumber = int(input("Enter a number: "))

for i in range(len(array)):
  if array[i] > chosenNumber:
    print(array[i])