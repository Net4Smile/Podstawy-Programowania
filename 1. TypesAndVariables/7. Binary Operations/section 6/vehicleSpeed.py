maxSpeed = 140
minSpeed = 40
speed = int(input('Enter vehicle speed: '))

speedOk = speed >= minSpeed and speed <= maxSpeed

print(f'Speed is valid: {speedOk}')
