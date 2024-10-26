def f(amount_to_pay: int):
  coins = 0
  while amount_to_pay > 0:
    if amount_to_pay - 5 >= 0:
      amount_to_pay -= 5
      coins += 1
    elif amount_to_pay - 2 >= 0:
      amount_to_pay -= 2
      coins += 1
    elif amount_to_pay - 1 >= 0:
      amount_to_pay -= 1
      coins += 1
  return coins

print(f(26))
print(f(8))
print(f(1))
print(f(0))