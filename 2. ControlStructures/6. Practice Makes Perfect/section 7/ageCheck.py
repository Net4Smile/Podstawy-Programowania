age = int(input('Enter your age: '))

ageGroup = ''

if age < 13:
  ageGroup = 'child'
elif age >= 13 and age <= 19:
  ageGroup = 'teen'
elif age >= 20 and age <= 64:
  ageGroup = 'adult'
elif age >= 65:
  ageGroup = 'senior'

print(f'You are a {ageGroup}')