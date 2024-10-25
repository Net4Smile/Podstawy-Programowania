import random

randomNumber = random.randint(1, 6)

specialNumber = randomNumber == 6 or randomNumber == 1

print(f"Dice rolled: {randomNumber}")
print(f"Special dice (1 or 6): {specialNumber}")