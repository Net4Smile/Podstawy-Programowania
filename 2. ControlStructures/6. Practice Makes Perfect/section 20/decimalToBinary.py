decimalNumber = int(input('Enter decimal number: '))

binaryNumber = ''

while decimalNumber > 0:
  remainder = decimalNumber % 2
  binaryNumber = str(remainder) + binaryNumber
  decimalNumber = decimalNumber // 2

print(f'Binary number: {binaryNumber}')