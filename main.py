import math
import triangle
import os

def area_of_circle(r):
    return math.pi * r ** 2

def area_of_semicircle(r):
    return (math.pi * r ** 2) / 2

def area_of_quarter_circle(r):
    return (math.pi * r ** 2) / 4

def radius_from_area(area):
    return math.sqrt(area / math.pi)

def radius_from_perimeter(p):
    return p / (2*math.pi)

def radius_from_diameter(d):
    d / 2

def quarter_circle_perimeter(r):
    return (math.pi * r / 2) + (2 * r)

def circumference(r):
    return 2 * math.pi * r

def semicircle_perimeter(r):
    return math.pi * r + 2 * r

def diameter(r):
    return 2 * r

def surface_area_cube(a):
    return 6 * a ** 2

def surface_area_open_cube(a):
    return 5 * a ** 2

def volume_cylinder(r, h):
    return math.pi * r ** 2 * h

def half_volume_cylinder(r, h):
    return (math.pi * r ** 2 * h) / 2

def third_volume_cylinder(r, h):
    return (math.pi * r ** 2 * h) / 3

def volume_cube(a):
    return a ** 3

def half_surface_area_cube(a):
    return 3 * a ** 2

def area_square(a):
    return a ** 2

def surface_area_open_cylinder(r, h):
    # Open at one end: 1 base + lateral
    base = math.pi * r ** 2
    lateral = 2 * math.pi * r * h
    return base + lateral

def menu():
    print("\nChoose calculation:")
    print("1. Area of a circle")
    print("2. Area of a semicircle")
    print("3. 1/4 the area of a circle")
    print("4a. Radius from area of a circle")
    print("4b. Radius from perimeter of a circle")
    print("4c. Radius from diameter of a circle")
    print("5. Perimeter of 1/4 of a circle")
    print("6. Perimeter of a circle")
    print("7. Perimeter of a semicircle")
    print("8. Diameter of a circle")
    print("9. Surface area of a cube")
    print("10. Surface area of cube (1 open side)")
    print("11. Volume of a cylinder")
    print("12. 1/2 the volume of a cylinder")
    print("13. 1/3 the volume of a cylinder")
    print("14. Volume of a cube")
    print("15. 1/2 the surface area of a cube")
    print("16. Area of a square")
    print("17. Surface area of an open cylinder (one end open)")
    print("18. Type of triangle calculation")
    print("0. Exit")

def main():
    while True:


        menu()
        choice = input("Enter choice: ")
        try:
            if choice == '1':
                r = float(input("Radius: "))
                print("Area of circle:", area_of_circle(r))
            elif choice == '2':
                r = float(input("Radius: "))
                print("Area of semicircle:", area_of_semicircle(r))
            elif choice == '3':
                r = float(input("Radius: "))
                print("1/4 Area of circle:", area_of_quarter_circle(r))
            elif choice == '4a':
                area = float(input("Area: "))
                print("Radius:", radius_from_area(area))
            elif choice == '4b':
                p = float(input("Perimeter: "))
                print("Radius:", radius_from_perimeter(p))
            elif choice == '4c':
                d = float(input("Diameter: "))
                print("Radius:", radius_from_diameter(d))
            elif choice == '5':
                r = float(input("Radius: "))
                print("Perimeter of 1/4 circle:", quarter_circle_perimeter(r))
            elif choice == '6':
                r = float(input("Radius: "))
                print("Perimeter (circumference):", circumference(r))
            elif choice == '7':
                r = float(input("Radius: "))
                print("Perimeter of semicircle:", semicircle_perimeter(r))
            elif choice == '8':
                r = float(input("Radius: "))
                print("Diameter:", diameter(r))
            elif choice == '9':
                a = float(input("Side: "))
                print("Surface area of cube:", surface_area_cube(a))
            elif choice == '10':
                a = float(input("Side: "))
                print("Surface area open cube:", surface_area_open_cube(a))
            elif choice == '11':
                r = float(input("Radius: "))
                h = float(input("Height: "))
                print("Volume of cylinder:", volume_cylinder(r, h))
            elif choice == '12':
                r = float(input("Radius: "))
                h = float(input("Height: "))
                print("1/2 Volume of cylinder:", half_volume_cylinder(r, h))
            elif choice == '13':
                r = float(input("Radius: "))
                h = float(input("Height: "))
                print("1/3 Volume of cylinder:", third_volume_cylinder(r, h))
            elif choice == '14':
                a = float(input("Side: "))
                print("Volume of cube:", volume_cube(a))
            elif choice == '15':
                a = float(input("Side: "))
                print("1/2 Surface area of cube:", half_surface_area_cube(a))
            elif choice == '16':
                a = float(input("Side: "))
                print("Area of square:", area_square(a))
            elif choice == '17':
                r = float(input("Radius: "))
                h = float(input("Height: "))
                print("Surface area of open cylinder:", surface_area_open_cylinder(r, h))
            elif choice == '18':
                triangle.main()

            elif choice == '0':
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
