import math

def calculate_area(radius):
    return math.pi * radius**2

def calculate_circumference(radius):
    return 2 * math.pi * radius

if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle: "))
    
    area = calculate_area(radius)
    circumference = calculate_circumference(radius)
    
    print(f"Area of the circle: {area}")
    print(f"Circumference of the circle: {circumference}")




