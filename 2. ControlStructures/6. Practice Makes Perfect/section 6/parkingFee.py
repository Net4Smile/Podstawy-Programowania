amountOfHoursParked = int(input('Enter the number of hours parked: '))

if amountOfHoursParked >= 1 and amountOfHoursParked < 3:
  print('Parking fee is 5 PLN')
elif amountOfHoursParked >= 3 and amountOfHoursParked < 6:
  print('Parking fee is 15 PLN')
elif amountOfHoursParked > 6:
  print('Parking fee is 20 PLN')