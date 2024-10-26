fullTime = input('Enter time (24 hour format): ')

hours = int(fullTime[:2])
minutes = int(fullTime[3:5])

if hours > 12:
    hours -= 12
    print(f"Time in 12-hour format: {hours}:{minutes} PM")
else:
    print(f"Time in 12-hour format: {hours}:{minutes} AM")