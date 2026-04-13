import turtle
import math

def draw_polygon(sides, length=100):
    """Draws a regular polygon based on side count."""
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(length)
        turtle.right(angle)

def analyze_quadrilateral(): 
    
    print("Let's identify the specific type of quadrilateral.")
    all_sides_equal = input("Are all four sides equal? (yes/no): ").lower() == 'yes'
    all_angles_equal = input("Are all four angles equal (90 degrees)? (yes/no): ").lower() == 'yes'
    
    if all_sides_equal and all_angles_equal:
        return "Square"
    elif all_angles_equal:
        return "Rectangle"
    elif all_sides_equal:
        return "Rhombus"
    
    parallel_sides = input("Are opposite sides parallel? (yes/no): ").lower() == 'yes'
    if parallel_sides:
        return "Parallelogram"
    
    one_pair_parallel = input("Is at least one pair of sides parallel? (yes/no): ").lower() == 'yes'
    if one_pair_parallel:
        return "Trapezium/Trapezoid"
    
    return "Generic Quadrilateral"

def main():
   
    screen = turtle.Screen()
    screen.title("Polygon Drawer")
    
    try:
        sides = int(input("Enter the number of sides: "))
    except ValueError:
        print("Please enter a valid number.")
        return

  
    if sides == 3:
        print("Shape: Triangle")
        draw_polygon(sides)
    elif sides == 4:
        quad_type = analyze_quadrilateral()
        print(f"Shape: {quad_type}")
        # Specialized drawing for types could be added here
        draw_polygon(sides)
    elif sides == 5:
        print("Shape: Pentagon")
        draw_polygon(sides)
    elif sides == 6:
        print("Shape: Hexagon")
        draw_polygon(sides)
    else:
        print("Shape: Unknown / Other Polygon")
        if sides > 2:
            draw_polygon(sides)
        else:
            print("Not a valid polygon shape.")

    # Keep window open
    turtle.done()

if __name__ == "__main__":
    main()


