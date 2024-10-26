car_speed = int(input('Enter car speed: '))
speed_limit_min = 40
speed_limit_max = 140

if not car_speed >= speed_limit_min and not car_speed <= speed_limit_max:
  print('Warning: invalid car speed!!')