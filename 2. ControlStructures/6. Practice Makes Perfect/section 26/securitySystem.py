triesLeft = 3
correctPin = "0805"

pin = input('Enter PIN code: ')

while triesLeft > 0:
  if pin != correctPin:
    print("Incorrect...")
    triesLeft -= 1
    if (triesLeft == 0):
      print("Sorry, your payment card has been blocked.")
    pin = input('Enter PIN code: ')
  else:
    break
