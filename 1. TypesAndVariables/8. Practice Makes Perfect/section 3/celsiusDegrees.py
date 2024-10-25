###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# Takes input with decimals that is a celsius temperature
celsius = float(input('Enter temperature in degrees Celsius: '))

# Converts celsius to kelvin
kelvin = celsius + 273.15

# Converts celsius to fahrenheit
fahrenheit = (celsius * 1.8) + 32

# Prints celsius, kelvin, and fahrenheit
print(f'Celsius: {celsius}')
print(f'Kelvin: {kelvin}')
print(f'Fahrenheit: {fahrenheit}')