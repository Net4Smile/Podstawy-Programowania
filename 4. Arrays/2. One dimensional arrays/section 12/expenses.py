categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

expense_categories = []
for i in range(len(categories)):
  expense_categories.append(categories[i] + ": " + str(expenses[i]))
  

print(expense_categories)