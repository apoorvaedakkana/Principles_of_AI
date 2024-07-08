import math

def calculate_cylinder_volume(radius, height):
    volume = math.pi * (radius ** 2) * height
    return volume

radius = 3
height = 5
volume = calculate_cylinder_volume(radius, height)
print(f"Volume of the cylinder: {volume:.2f}")
