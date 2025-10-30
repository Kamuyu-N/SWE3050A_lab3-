def triangle_type(a, b, c):
    # Step 1: Validate input (positive sides)
    if a <= 0 or b <= 0 or c <= 0:
        return "Error: Side lengths must be positive integers that are greater than 0."

    # Step 2: Determine type
    if a == b and b == c:
        return "Equilateral Triangle: All sides are equal."
    elif a == b or b == c or a == c:
        return "Isosceles Triangle: Exactly two sides are equal."
    elif a != b and a != c and b != c:
        return "Scalene Triangle: All sides are different."
    else:
        return "Error"


# Main program
def main():
    try:
        print("Enter three integers representing the sides of the triangle:")
        a = int(input("Side a: "))
        b = int(input("Side b: "))
        c = int(input("Side c: "))

        result = triangle_type(a, b, c)
        print(result)

    except ValueError:
        print("Error: Please enter valid integers only.")


if __name__ == "__main__":
    main()