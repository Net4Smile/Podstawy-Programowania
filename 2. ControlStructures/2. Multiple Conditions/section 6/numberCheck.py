number = int(input('Enter number: '))

if number < 0:
  print(f'{number} is negative')
elif number == 0:
  print(f'{number} is 0')
elif number > 0:
  print(f'{number} is positive')