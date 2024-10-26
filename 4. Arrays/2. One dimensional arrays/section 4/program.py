###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
print('Last value but one value', arr[4])
print('Sum of first and last values', arr[0] + arr[-1])
print('Middle value', arr[2])

arrayWithSpaces = ""
for i in range(len(arr)):
  arrayWithSpaces += f"{arr[i]} "

print(arrayWithSpaces)