###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

def checkPin(pinToCheck):
  if pinToCheck == pin:
      print("PIN code is correct. Processing...")
      return True
  else:
      print("Incorrect PIN code. Please try again.")
      return False
  

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Change PIN")
    print("5. Exit")

    choice = input("Choose an option (1-4): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        getPin = input("Enter the PIN code: ")
        if not checkPin(getPin):
          continue
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        getPin = input("Enter the PIN code: ")
        if not checkPin(getPin):
          continue
        newPin = input("Enter the new PIN code: ")

        if len(newPin) == 4 and newPin.isdigit():
            pin = newPin
            print("PIN code has been changed.")
            print(f"New PIN code: {pin}")
        else:
            print("Invalid PIN code. Please try again.")
            continue            
    elif choice == '5':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    else:
        print("Invalid option. Please try again.")