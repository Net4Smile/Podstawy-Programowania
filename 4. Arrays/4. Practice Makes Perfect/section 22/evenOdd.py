array = [15, 38, 7, 23, 14]

even = []
odd = []

for i in range(len(array)):
  if array[i] % 2 == 0:
    even.append(array[i])
  elif array[i] % 2 == 1:
    odd.append(array[i])

print("Even numbers:", ' '.join(map(str, even)))
print("Odd numbers:", ' '.join(map(str, odd)))
