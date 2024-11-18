import argparse
import math

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Calculate area and perimeter of a circle.")
    
    # Add the radius argument
    parser.add_argument("radius", type=float, help="The radius of the circle")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Get the radius value from the argument
    radius = args.radius
    
    # Calculate area and perimeter
    area = math.pi * radius**2
    perimeter = 2 * math.pi * radius
    
    # Output the results
    print(f"Radius: {radius}")
    print(f"Area of the circle: {area:.2f}")
    print(f"Perimeter of the circle: {perimeter:.2f}")

if __name__ == "__main__":
    main()
