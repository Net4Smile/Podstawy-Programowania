# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   total = 0
   for row in seats:
      for place in row:
            total += 1
            
   return total

def seats_available(seats):
   totalAvailable = 0
   for row in seats:
       for place in row:
           if place == 'A':
               totalAvailable += 1

   return totalAvailable

def seats_booked(seats):
   totalBooked = 0
   for row in seats:
       for place in row:
           if place == 'B':
               totalBooked += 1
   return totalBooked

def seat_status(seats, row, place):
  for index in range(len(seats)):
    if index == row - 1:
      for index2 in range(len(seats[index])):
         if index2 == place - 1:
            return seats[index][index2]

print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))