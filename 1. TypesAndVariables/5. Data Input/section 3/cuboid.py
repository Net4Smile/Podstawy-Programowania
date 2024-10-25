###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=')
b = input('b=')
c = input('c=')
cuboid_volume = a * b * c
cuboid_surface_area = 2 * (a * b + a * c + b * c)
print(f'The volume of the cuboid is {cuboid_volume}.')
print(f'The surface area of the cuboid is {cuboid_surface_area}.')