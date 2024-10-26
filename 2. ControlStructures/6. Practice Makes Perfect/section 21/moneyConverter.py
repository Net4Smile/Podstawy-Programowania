amount = float(input('Enter amount in PLN: '))

piatka = 0
dwojka = 0
jedynka = 0

while amount > 0:
  if amount - 5 >= 0:
    piatka += 1
    amount -= 5
    continue
  if amount - 2 >= 0:
    dwojka += 1
    amount -= 2
    continue
  if amount - 1 >= 0:
    jedynka += 1
    amount -= 1

print(f"The amount of PLN {amount} in coins: ")
print(f"5 PLN coins: {piatka}")
print(f"2 PLN coins: {dwojka}")
print(f"1 PLN coins: {jedynka}")