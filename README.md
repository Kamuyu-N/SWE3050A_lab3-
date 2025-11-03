# LAB3 ASSIGMENT

## Overview

This project implements 17 different geometry calculations and integrates them with a triangle classification system. The program provides a user-friendly menu-driven interface for performing calculations and includes comprehensive test coverage to ensure accuracy and reliability.

## Features

### Geometry Calculations

**Circle Operations:**
- Area of a circle
- Area of a semicircle
- Area of a quarter circle (1/4 circle)
- Radius calculation from area, perimeter, or diameter
- Perimeter calculations (full circle, semicircle, quarter circle)
- Diameter calculation

**Cube Operations:**
- Surface area of a cube
- Surface area of a cube with one open side
- Volume of a cube
- Half surface area of a cube

**Cylinder Operations:**
- Volume of a cylinder
- Half volume of a cylinder
- One-third volume of a cylinder
- Surface area of an open cylinder

**Square Operations:**
- Area of a square

### Triangle Classification

- Determines triangle type based on side lengths:
  - Equilateral (all sides equal)
  - Isosceles (exactly two sides equal)
  - Scalene (all sides different)
- Input validation for edge cases

## Requirements

- Python 3.x
- Standard library modules: `math`, `unittest`

## Installation

1. Clone or download this repository
2. Ensure Python 3.x is installed on your system
3. No additional dependencies required

## Usage

### Running the Program

```bash
py main.py
```

Or alternatively:
```bash
python main.py
```
or
```bash
python3 main.py
```

### Using the Menu

Once the program starts, you will see a menu with numbered options. Simply:
1. Enter the number corresponding to your desired calculation
2. Follow the prompts to enter required values
3. View the calculated result
4. Choose another calculation or exit (option 0)

### Example Session

```
Choose calculation

1.  Area of a circle                          2.  Area of a semicircle                       3.  1/4 area of a circle
...

Enter choice: 1
Radius: 5
Area of circle: 78.53981633974483
```

## Project Structure

```
├── main.py          # Main program with geometry functions and menu interface
├── triangle.py      # Triangle type determination module
├── test_main.py     # Comprehensive test suite
├── test.md          # Detailed test documentation
└── README.md        # This file
```

## Testing

The project includes a comprehensive test suite with **72 test cases** covering:
- 40 tests for geometry functions
- 10 tests for triangle functions
- 22 tests for integrated functionality

### Running Tests

```bash
py -m unittest test_main.py -v
```

For detailed information about the test cases, see [test.md](test.md).

## Assignment Requirements

### Task 1: Geometry Program

**Part i) - Implementation:**
1. Area of a circle
2. Area of a semicircle
3. 1/4 the area of a circle
4. The radius of a circle (from area, perimeter, or diameter)
5. The perimeter of a ¼ of a circle
6. The perimeter of a circle
7. The perimeter of a semicircle
8. The diameter of a circle
9. The surface area of a cube
10. The surface area of a cube with one open side
11. The volume of a cylinder
12. ½ the volume of a cylinder
13. 1/3 the volume of a cylinder
14. The volume of a cube
15. ½ The surface area of a cube
16. The area of a square
17. The surface area of an open cylinder

**Part ii) - Testing:**
- Implemented 40 test cases for the geometry program (exceeds requirement of 20+)

### Task 2: Integration

**Task 2.1 - Integration:**
- Integrated geometry program with triangle classification program
- Access triangle calculations via menu option 18

**Task 2.2 - Integrated Testing:**
- Implemented 22 test cases for the integrated program (exceeds requirement of 20+)

## Development

### Code Quality

- Functions are modular and well-documented
- Error handling implemented for edge cases
- Consistent code style throughout

### Testing Strategy

- Unit tests for individual functions
- Integration tests for combined functionality
- Edge case coverage (zero values, large numbers)
- Relationship validation (e.g., semicircle = half circle)


## Contributors

Group project - SWE3050A Lab 3
