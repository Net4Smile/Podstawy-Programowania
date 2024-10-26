productsPurchased = int(input('Number of products purchased: '))
productPrice = int(input('Product price: '))
priceToPay = 0

for i in range(productsPurchased):
  if productsPurchased > 2:
    priceToPay = productPrice - (productPrice * 0.25)
  else:
    priceToPay = productPrice

print(f'Amount to pay: {priceToPay}')