

x = int(input("What is the length of the first side "))  # CASTING
y = int(input("What is the length of the second side "))

def square_area(side1, side2):
  area = side1 * side2
  print(f"The area is {area}")

  return area

square_area(x, y)



b = int(input("What is the base of the triangle "))
h = int(input("What is the height of the triangle "))

def triangle_area(height, base):
  triangle = (b * h) / 2
  print(f"The area of the triangle is {triangle}")

  return triangle

triangle_area(h, b)



r = int(input("What is the radius of the circle "))
pi = 3.14159256

def circle_area(radius, pie):
  circle_Area = pi * r * r
  print(f"The Area of the circle is {circle_Area}") 

  return circle_Area

circle_area(r, pi)