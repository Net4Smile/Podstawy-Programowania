# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements

food = 0
transport = 0
utilities = 0

for i in range(len(monthly_expenses)):
  food += monthly_expenses[i][0]
  transport += monthly_expenses[i][1]
  utilities += monthly_expenses[i][2]

weekOne = sum(monthly_expenses[0])
weekTwo = sum(monthly_expenses[1])
weekThree = sum(monthly_expenses[2])
weekFour = sum(monthly_expenses[3])

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food)
print('Transport:', transport)
print('Utilities:', utilities)
print('Week 1:', weekOne)
print('Week 2:', weekTwo)
print('Week 3:', weekThree)
print('Week 4:', weekFour)
print('---------------')
print('TOTAL:', food + transport + utilities)