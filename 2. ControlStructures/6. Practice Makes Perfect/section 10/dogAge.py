# Write a program that calculates a dog's age in dog's years. For the first two years, a dog's life is equal to 10.5 human years. After that, each dog year is equal to 4 human years. Sample result:

# Enter the dog's age in human years: 15
# The dog's age in dog's years is 73 years.

dogAge = int(input('Enter the dog\'s age in human years: '))

dogAgeInDogYears = 0

for i in range(dogAge):
  if i < 2:
    dogAgeInDogYears += 10.5
  else:
    dogAgeInDogYears += 4

print(f'The dog\'s age in dog\'s years is {dogAgeInDogYears} years.')

