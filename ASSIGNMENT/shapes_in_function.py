
# Shapes in Functions


# Circle
def circle_details(radius):
    circumference = 2 * 3.14 * radius
    area_circle = 3.14 * radius**2
    return circumference, area_circle

radius = 5
circumference_result, area_circle = circle_details(radius)
   
print(f"Circumference: {circumference_result:.2f}")
print(f"Area: {area_circle:.2f}")
print()



# Square
def geometry(side_length, circle_radius):
    # Calculate perimeter of the square 
    square_perimeter = 4 * side_length
    # Calculate area of the square
    square_area = side_length**2
    # Calculate circumference of the circle
    circle_circumference = 2 * 3.14 * radius
    # Calculate area of the circle
    circle_area = 3.14 * circle_radius**2 


    # Compare and print the results
    if square_perimeter > circle_circumference:
        print("The square has a larger perimeter.")
    elif square_perimeter < circle_area:
        print("The circle has a larger circumference.")
    else:
        print("Both the square and the circle have the same perimeter.")

    if square_area > circle_area:
        print("The square has a larger area.")
    elif square_area < circle_circumference:
        print("The circle has larger area.")
    else:
        print("Both the square and the circle have the same area.")

side_length = 9
circle_radius = 3
geometry(side_length, circle_radius)
