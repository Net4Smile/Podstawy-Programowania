eanNumber = input('Enter EAN number: ')

if len(eanNumber) == 13 and eanNumber.isdigit():
  print(f"Article number is correct")
  firstThreeDigits = eanNumber[:3]
  if firstThreeDigits == "590":
    print(f"Article manufactured in Poland")
