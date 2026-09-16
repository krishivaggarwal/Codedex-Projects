# The Introduction
print("==================================== \n Area Calculator \n====================================")

# Which shape?
shape = int(input("What shape do you want to calculate the area for? \n1. Triangle \n2. Rectangle \n3. Square \n4. Circle \nEnter 1, 2, 3 or 4: "))

if shape == 1:
    # Triangle
    base = float(input("base: "))
    height = float(input("height: "))
    area = 0.5 * base * height
    print(f"The area is: {area}")

elif shape == 2:
    # Rectangle
    length = float(input("length: "))
    width = float(input("width: "))
    area = length * width
    print(f"The area is: {area}")

elif shape == 3:
    # Square
    side = float(input("side: "))
    area = side ** 2
    print(f"The area is: {area}")

elif shape == 4:
    # Circle
    import math
    radius = float(input("radius: "))
    area = math.pi * (radius ** 2)
    print(f"The area is: {area}")