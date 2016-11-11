import math

# Area of the circle by taking input of radius from the end user

# use input function to get input in radians

r = float(input('What is the radius of the circle?\n'))

area = math.pi * (r ** 2)  # Calculating area of the circle

print("Area of the circle is: ", area)
