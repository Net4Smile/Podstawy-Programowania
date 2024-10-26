import calculations

string = input('Enter string: ')
letterToCheck = input('Enter letter to count: ')

specificCharacterCount = calculations.calculate(string, letterToCheck)

print(f"The number of letter 'e': {specificCharacterCount}")