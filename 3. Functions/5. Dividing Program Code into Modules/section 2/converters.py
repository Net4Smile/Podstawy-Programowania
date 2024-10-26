def m_to_cm(n):
  return n * 100

def cm_to_m(n):
  return n / 100

def cm_to_inches(n):
  return n / 2.54

def feet_and_inches_to_cm(feet, inches):
  return feet * 12 + inches


if __name__ == "__main__":
  # only execute when you run this module
  # so you can test the functions in this place
  print(f'2m = {m_to_cm(2)}cm')
  print(f'532cm = {cm_to_m(532)}m')
  print(f'1.5m = {cm_to_inches(1.5)}in')
  print(f'1ft 2in = {feet_and_inches_to_cm(1, 2)}cm')

