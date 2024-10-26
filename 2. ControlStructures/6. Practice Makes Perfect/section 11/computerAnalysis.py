previousProductPrice = 200.00
currentProductPrice = 140.00

percentageDecrease = ((currentProductPrice - previousProductPrice) / previousProductPrice) * 100

if percentageDecrease >= 10:
  print(f"Buy the product!!")
  print(f"Product price reduced by {percentageDecrease}%")