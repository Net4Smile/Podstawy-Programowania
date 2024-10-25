import math

height = float(input("Enter your height in meters: "))

distance = 3.57 * math.sqrt(height)

print("The distance to the horizon is", distance, "km")