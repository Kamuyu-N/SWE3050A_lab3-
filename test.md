# Test Documentation

## Overview

This document explains the test cases we created for our geometry and triangle calculation program. We have **72 test cases total** that verify all functions work correctly.

## Test Structure

Our tests are organized into 3 main groups:

### 1. Geometry Functions Tests (40 tests)

These test all 17 geometry functions in `main.py`:

**Circle Calculations:**
- Area of circle (basic, zero, large numbers)
- Area of semicircle (should be half of full circle)
- Area of quarter circle (should be 1/4 of full circle)
- Radius calculations (from area, from perimeter, from diameter)
- Perimeter calculations (full circle, semicircle, quarter circle)
- Diameter calculations

**Cube Calculations:**
- Surface area of cube
- Surface area of cube with one open side
- Volume of cube
- Half surface area of cube

**Cylinder Calculations:**
- Volume of cylinder
- Half volume of cylinder
- Third volume of cylinder
- Surface area of open cylinder

**Square Calculations:**
- Area of square

**What these tests check:**
- Basic calculations work correctly
- Edge cases like zero values
- Relationships (e.g., semicircle = half circle)
- Roundtrip tests (calculate area, then get radius back - should match)

### 2. Triangle Functions Tests (10 tests)

These test the triangle type determination in `triangle.py`:

- **Equilateral triangle** (all sides equal)
- **Isosceles triangle** (two sides equal) - tests all combinations
- **Scalene triangle** (all sides different)
- **Error cases** (zero sides, negative sides)
- **Large numbers** (to make sure it works with big values)

**What these tests check:**
- Correctly identifies triangle types
- Handles invalid inputs properly

### 3. Integrated Program Tests (22 tests)

These test that geometry and triangle functions work together:

- Combining circle and triangle calculations
- Using results from one calculation in another
- Making sure functions don't interfere with each other
- Testing relationships between different calculations (e.g., checking that volume fractions are correct)
- Error handling when one part fails but others should still work

**What these tests check:**
- Everything works when used together
- Calculations are consistent
- The integration is stable

## How to Run the Tests

Run this command in your terminal:

```bash
py -m unittest test_main.py -v
```

(**NOTE**: python3 or python may be used if py does not work on your computer.)

The `-v` flag shows detailed output for each test.

**Expected Output:**
- You should see "Ran 72 tests"
- All tests should show "ok"
- If any test fails, you'll see which one and why

## Test Requirements Summary

According to the assignment requirements:

- ✅ **Part ii):** Write at least 20 test cases for the geometry program
  - We have **40 test cases** for geometry functions
  
- ✅ **Task 2.2:** Write at least 20 test cases for the integrated program
  - We have **22 test cases** for integrated functionality

## Key Test Concepts Explained

### Basic Tests
These just check if a function gives the right answer for a simple input.
Example: `test_area_of_circle_basic` checks if area of circle with radius 5 is correct.

### Edge Case Tests
These test special situations like zero values or very large numbers.
Example: `test_area_of_circle_zero` checks if the function handles radius = 0 correctly.

### Relationship Tests
These verify that related functions give consistent results.
Example: `test_area_of_semicircle_relation_to_full` checks if semicircle area is exactly half of full circle area.

### Roundtrip Tests
These check if you can go from A → B → A and get back to the original value.
Example: `test_radius_from_area_roundtrip` calculates area from radius, then calculates radius from that area, and checks if we get the original radius back.

## Files Involved

- `test_main.py` - Contains all our test cases
- `main.py` - Contains the 17 geometry functions we're testing
- `triangle.py` - Contains the triangle type function we're testing

## Notes

- All tests use `assertAlmostEqual` for floating-point comparisons (because of rounding)
- Tests are named clearly so you can understand what each one does
- Tests are organized by what they test (geometry, triangle, or integration)
- We test both normal cases and edge cases to make sure the program is robust

## Quick Reference

| Category | Number of Tests | Purpose |
|----------|----------------|---------|
| Geometry Functions | 40 | Test all 17 geometry calculations |
| Triangle Functions | 10 | Test triangle type determination |
| Integrated Tests | 22 | Test geometry + triangle together |
| **Total** | **72** | **Complete test coverage** |

