def f(dice: str):
  mostRolled = {}
  for char in dice:
    mostRolled[char] = dice.count(char)

  maxRoll = max(mostRolled, key=mostRolled.get)

  return maxRoll

    
    

print(f("5233165554211"))
print(f("2133"))