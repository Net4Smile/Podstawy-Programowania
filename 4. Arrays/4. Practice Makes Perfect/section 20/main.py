import MyArrays

array = [7, 3, 8, 5, 2]

print("Numbers: " + ", ".join(map(str, array)))
print("Second largest number: " + str(MyArrays.secondLargest(array)))
print("Median: " + str(MyArrays.median(array)))
print("Smallest and largest number: " + str(MyArrays.minMaxOneArray(array)))
print("Numbers as a string: " + MyArrays.arrayAsString(array))