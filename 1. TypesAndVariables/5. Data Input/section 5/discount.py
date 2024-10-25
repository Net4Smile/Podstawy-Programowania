price = round(float(input('Enter price: ')), 2)
discount = float(input('Enter discount %: '))

discounted_price = price - (price * discount / 100)

print(f'Price with discount: {discounted_price}')
print(f"Reduction: {price - discounted_price}")
