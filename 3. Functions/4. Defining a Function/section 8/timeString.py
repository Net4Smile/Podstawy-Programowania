def time_string(hours: int, minutes: int, time_format: str):
  if time_format == '12':
    if hours > 12:
      hours -= 12
      if minutes < 10:
        minutes = '0' + str(minutes)
      return f'{hours}:{minutes} PM'
    else:
      if minutes < 10:
        minutes = '0' + str(minutes)
      return f'{hours}:{minutes} AM'
  elif time_format == '24':
    if minutes < 10:
      minutes = '0' + str(minutes)
    return f'{hours}:{minutes}'
  
print(time_string(15, 38, '24'))
print(time_string(8, 3, '24'))
print(time_string(0, 5, '24'))
print(time_string(11, 15, '12'))
print(time_string(0, 7, '12'))
print(time_string(7, 30, '12'))
print(time_string(12, 46, '12'))
print(time_string(13, 10, '12'))
print(time_string(19, 2, '12'))