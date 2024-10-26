# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]

# Returns a week day name
def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n - 1]

# Returns a string with day meal names
# separated by comma
def day_meal_plan(meal_plan, day_number):
   day_meal_plan = ''
   for meal in meal_plan[day_number - 1]:
      day_meal_plan += meal + ', '

      if meal_plan[day_number - 1][-1] == meal:
         day_meal_plan = day_meal_plan[:-2]
       
   return day_meal_plan

# Prints weekly meal plan
print('WEEKLY MEAL PLAN')
print('(Breakfast, Lunch, Dinner)')
print('==========================')
for day in range(1, 8):
   print(weekday(day) + ':', day_meal_plan(meal_plan, day))
   print()