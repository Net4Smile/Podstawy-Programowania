import range

rangeX = 1
rangeY = 10
number = 5

if range.isInRange(rangeX, rangeY, number):
  print(f'Number {number} in range <{rangeX}, {rangeY}: yes>')
else:
  print(f'Number {number} in range <{rangeX}, {rangeY}: no>')