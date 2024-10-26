def secondLargest(array):
  if len(array) == 0:
    return None
  
  largest = 0
  secondLargest = 0

  for i in range(len(array)):
    if array[i] > largest:
      secondLargest = largest
      largest = array[i]
      continue
    if array[i] > secondLargest:
      secondLargest = array[i]
      continue

  return secondLargest
  

def differenceBetweenMinAndMax(array):
  if len(array) == 0:
    return None
  
  minValue = array[0]
  maxValue = array[0]
  for i in range(1, len(array)):
    if array[i] < minValue:
      minValue = array[i]
      maxValue = array[i]
      continue
    if array[i] > maxValue:
      maxValue = array[i]
      continue
    if array[i] > minValue and array[i] < maxValue:
      return array[i] - minValue

def median(array):
  if len(array) == 0:
    return None
  
  sortedArray = sorted(array)
  middle = len(sortedArray) // 2
  if len(sortedArray) % 2 == 0:
    return (sortedArray[middle - 1] + sortedArray[middle]) / 2
  else:
    return sortedArray[middle]
  
def minMaxOneArray(array):
  if len(array) == 0:
    return None
  
  minValue = array[0]
  maxValue = array[0]
  for i in range(1, len(array)):
    if array[i] < minValue:
      minValue = array[i]
    if array[i] > maxValue:
      maxValue = array[i]

  return str(minValue) + ", " + str(maxValue)

def arrayAsString(array):
  string = ""
  for i in range(len(array)):
    if i == len(array) - 1:
      string += str(array[i])
    else:
      string += str(array[i]) + "-"
    
  return string
