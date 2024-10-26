###
# Program for testing built-in functions
#
max_number = max(7, 5, 6, 3, 8, 2)
print('Max number of 7, 5, 6, 3, 8, 2 is', max_number)

min_number = min(4, 7, 2, 3, 9, 8)
print('Min number of 4, 7, 2, 3, 9, 8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

fromKeyboard = input('Enter a letter: ')
print('The letter you entered is', fromKeyboard)

string = "20303"
number = chr(int(string))
print(f'The number from string {string} is', number)

decimalNumber = 304
binaryNumber = bin(decimalNumber)
print(f'The binary number of {decimalNumber} is {binaryNumber}')

hexadecimalNumber = hex(decimalNumber)
print(f'The hexadecimal number of {decimalNumber} is {hexadecimalNumber}')

euroSign = ord('€')
print(f'The code of the euro sign is {euroSign}')

absoluteValue = abs(-17)
print(f'The absolute value of -17 is {absoluteValue}')