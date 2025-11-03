import unittest
import math
import main
import triangle


class TestGeometryFunctions(unittest.TestCase):
    """Test cases for all 17 geometry functions"""

    # Test 1: Area of a circle
    def test_area_of_circle_basic(self):
        self.assertAlmostEqual(main.area_of_circle(5), math.pi * 25, places=5)

    def test_area_of_circle_zero(self):
        self.assertEqual(main.area_of_circle(0), 0)

    def test_area_of_circle_large(self):
        self.assertAlmostEqual(main.area_of_circle(100), math.pi * 10000, places=2)

    # Test 2: Area of a semicircle
    def test_area_of_semicircle_basic(self):
        self.assertAlmostEqual(main.area_of_semicircle(4), (math.pi * 16) / 2, places=5)

    def test_area_of_semicircle_relation_to_full(self):
        r = 5
        semicircle = main.area_of_semicircle(r)
        full_circle = main.area_of_circle(r)
        self.assertAlmostEqual(semicircle, full_circle / 2, places=5)

    # Test 3: 1/4 area of a circle
    def test_area_of_quarter_circle_basic(self):
        self.assertAlmostEqual(main.area_of_quarter_circle(6), (math.pi * 36) / 4, places=5)

    def test_area_of_quarter_circle_relation(self):
        r = 8
        quarter = main.area_of_quarter_circle(r)
        full = main.area_of_circle(r)
        self.assertAlmostEqual(quarter, full / 4, places=5)

    # Test 4: Radius from area
    def test_radius_from_area_basic(self):
        area = math.pi * 25  # circle with radius 5
        self.assertAlmostEqual(main.radius_from_area(area), 5, places=5)

    def test_radius_from_area_roundtrip(self):
        r = 7
        area = main.area_of_circle(r)
        self.assertAlmostEqual(main.radius_from_area(area), r, places=5)

    # Test 5: Radius from perimeter
    def test_radius_from_perimeter_basic(self):
        p = 2 * math.pi * 10  # circle with radius 10
        self.assertAlmostEqual(main.radius_from_perimeter(p), 10, places=5)

    def test_radius_from_perimeter_roundtrip(self):
        r = 6
        p = main.circumference(r)
        self.assertAlmostEqual(main.radius_from_perimeter(p), r, places=5)

    # Test 6: Radius from diameter
    def test_radius_from_diameter_basic(self):
        self.assertEqual(main.radius_from_diameter(20), 10)

    def test_radius_from_diameter_zero(self):
        self.assertEqual(main.radius_from_diameter(0), 0)

    def test_radius_from_diameter_odd_number(self):
        self.assertEqual(main.radius_from_diameter(15), 7.5)

    # Test 7: Perimeter of 1/4 circle
    def test_quarter_circle_perimeter_basic(self):
        r = 4
        expected = (math.pi * r / 2) + (2 * r)
        self.assertAlmostEqual(main.quarter_circle_perimeter(r), expected, places=5)

    def test_quarter_circle_perimeter_zero(self):
        self.assertEqual(main.quarter_circle_perimeter(0), 0)

    # Test 8: Perimeter of a circle (circumference)
    def test_circumference_basic(self):
        self.assertAlmostEqual(main.circumference(5), 2 * math.pi * 5, places=5)

    def test_circumference_zero(self):
        self.assertEqual(main.circumference(0), 0)

    # Test 9: Perimeter of a semicircle
    def test_semicircle_perimeter_basic(self):
        r = 5
        expected = math.pi * r + 2 * r
        self.assertAlmostEqual(main.semicircle_perimeter(r), expected, places=5)

    def test_semicircle_perimeter_relation_to_circumference(self):
        r = 6
        semicircle_perim = main.semicircle_perimeter(r)
        full_perim = main.circumference(r)
        # Semicircle perimeter should be half circumference + diameter
        expected = (full_perim / 2) + (2 * r)
        self.assertAlmostEqual(semicircle_perim, expected, places=5)

    # Test 10: Diameter of a circle
    def test_diameter_basic(self):
        self.assertEqual(main.diameter(5), 10)

    def test_diameter_zero(self):
        self.assertEqual(main.diameter(0), 0)

    # Test 11: Surface area of a cube
    def test_surface_area_cube_basic(self):
        self.assertEqual(main.surface_area_cube(5), 6 * 25)

    def test_surface_area_cube_zero(self):
        self.assertEqual(main.surface_area_cube(0), 0)

    # Test 12: Surface area of cube with one open side
    def test_surface_area_open_cube_basic(self):
        self.assertEqual(main.surface_area_open_cube(4), 5 * 16)

    def test_surface_area_open_cube_relation(self):
        a = 6
        open_cube = main.surface_area_open_cube(a)
        full_cube = main.surface_area_cube(a)
        self.assertEqual(open_cube, full_cube - (a ** 2))

    # Test 13: Volume of a cylinder
    def test_volume_cylinder_basic(self):
        self.assertAlmostEqual(main.volume_cylinder(3, 4), math.pi * 9 * 4, places=5)

    def test_volume_cylinder_zero_radius(self):
        self.assertEqual(main.volume_cylinder(0, 5), 0)

    def test_volume_cylinder_zero_height(self):
        self.assertEqual(main.volume_cylinder(5, 0), 0)

    # Test 14: 1/2 volume of cylinder
    def test_half_volume_cylinder_basic(self):
        r, h = 5, 10
        half_vol = main.half_volume_cylinder(r, h)
        full_vol = main.volume_cylinder(r, h)
        self.assertAlmostEqual(half_vol, full_vol / 2, places=5)

    # Test 15: 1/3 volume of cylinder
    def test_third_volume_cylinder_basic(self):
        r, h = 6, 9
        third_vol = main.third_volume_cylinder(r, h)
        full_vol = main.volume_cylinder(r, h)
        self.assertAlmostEqual(third_vol, full_vol / 3, places=5)

    # Test 16: Volume of a cube
    def test_volume_cube_basic(self):
        self.assertEqual(main.volume_cube(5), 125)

    def test_volume_cube_zero(self):
        self.assertEqual(main.volume_cube(0), 0)

    # Test 17: 1/2 surface area of cube
    def test_half_surface_area_cube_basic(self):
        self.assertEqual(main.half_surface_area_cube(4), 3 * 16)

    def test_half_surface_area_cube_relation(self):
        a = 5
        half_surface = main.half_surface_area_cube(a)
        full_surface = main.surface_area_cube(a)
        self.assertEqual(half_surface, full_surface / 2)

    # Test 18: Area of a square
    def test_area_square_basic(self):
        self.assertEqual(main.area_square(5), 25)

    def test_area_square_zero(self):
        self.assertEqual(main.area_square(0), 0)

    # Test 19: Surface area of open cylinder
    def test_surface_area_open_cylinder_basic(self):
        r, h = 3, 5
        expected = math.pi * r ** 2 + 2 * math.pi * r * h
        self.assertAlmostEqual(main.surface_area_open_cylinder(r, h), expected, places=5)

    def test_surface_area_open_cylinder_zero_radius(self):
        self.assertEqual(main.surface_area_open_cylinder(0, 5), 0)

    # Test 20: Edge case - negative radius (should handle or produce expected math result)
    def test_area_circle_negative_radius(self):
        # Squaring negative gives positive, so this is mathematically valid
        self.assertAlmostEqual(main.area_of_circle(-5), math.pi * 25, places=5)

    # Test 21: Large number handling
    def test_circumference_large_number(self):
        large_r = 1000000
        result = main.circumference(large_r)
        expected = 2 * math.pi * large_r
        self.assertAlmostEqual(result, expected, places=2)

    # Test 22: Decimal precision test
    def test_radius_from_area_precision(self):
        r = 3.14159
        area = main.area_of_circle(r)
        calculated_r = main.radius_from_area(area)
        self.assertAlmostEqual(calculated_r, r, places=5)


class TestTriangleFunctions(unittest.TestCase):
    """Test cases for triangle type determination"""

    def test_equilateral_triangle(self):
        result = triangle.triangle_type(5, 5, 5)
        self.assertIn("Equilateral", result)

    def test_isosceles_triangle_ab_equal(self):
        result = triangle.triangle_type(5, 5, 3)
        self.assertIn("Isosceles", result)

    def test_isosceles_triangle_bc_equal(self):
        result = triangle.triangle_type(3, 5, 5)
        self.assertIn("Isosceles", result)

    def test_isosceles_triangle_ac_equal(self):
        result = triangle.triangle_type(5, 3, 5)
        self.assertIn("Isosceles", result)

    def test_scalene_triangle(self):
        result = triangle.triangle_type(3, 4, 5)
        self.assertIn("Scalene", result)

    def test_triangle_zero_side(self):
        result = triangle.triangle_type(0, 4, 5)
        self.assertIn("Error", result)
        self.assertIn("positive", result)

    def test_triangle_negative_side(self):
        result = triangle.triangle_type(-1, 4, 5)
        self.assertIn("Error", result)

    def test_triangle_all_zero(self):
        result = triangle.triangle_type(0, 0, 0)
        self.assertIn("Error", result)

    def test_triangle_large_numbers(self):
        result = triangle.triangle_type(1000, 1000, 1000)
        self.assertIn("Equilateral", result)

    def test_triangle_different_large_numbers(self):
        result = triangle.triangle_type(100, 200, 300)
        self.assertIn("Scalene", result)


class TestIntegratedProgram(unittest.TestCase):
    """Test cases for integrated functionality combining geometry and triangle programs"""

    def test_geometry_and_triangle_separate_operations(self):
        # Test that geometry calculations don't interfere with triangle calculations
        circle_area = main.area_of_circle(5)
        triangle_result = triangle.triangle_type(3, 4, 5)
        self.assertGreater(circle_area, 0)
        self.assertIn("Scalene", triangle_result)

    def test_multiple_geometry_operations_sequence(self):
        # Sequential geometry calculations
        r = 5
        area = main.area_of_circle(r)
        perimeter = main.circumference(r)
        diameter = main.diameter(r)
        self.assertGreater(area, 0)
        self.assertGreater(perimeter, 0)
        self.assertEqual(diameter, 10)

    def test_circle_triangle_combined_scenario_1(self):
        # Scenario: Calculate circle area, then determine triangle type
        radius = 7
        circle_area = main.area_of_circle(radius)
        triangle_type_result = triangle.triangle_type(7, 7, 7)
        self.assertAlmostEqual(circle_area, math.pi * 49, places=5)
        self.assertIn("Equilateral", triangle_type_result)

    def test_circle_triangle_combined_scenario_2(self):
        # Calculate multiple circle properties and triangle
        r = 6
        area = main.area_of_semicircle(r)
        perimeter = main.semicircle_perimeter(r)
        triangle_result = triangle.triangle_type(6, 8, 10)
        self.assertGreater(area, 0)
        self.assertGreater(perimeter, 0)
        self.assertIn("Scalene", triangle_result)

    def test_cylinder_cube_triangle_combined(self):
        # Test cylinder, cube, and triangle calculations together
        cyl_vol = main.volume_cylinder(3, 4)
        cube_vol = main.volume_cube(3)
        triangle_result = triangle.triangle_type(3, 3, 4)
        self.assertGreater(cyl_vol, 0)
        self.assertGreater(cube_vol, 0)
        self.assertIn("Isosceles", triangle_result)

    def test_radius_calculations_consistency(self):
        # Test all three radius calculation methods give consistent results
        original_r = 5
        area = main.area_of_circle(original_r)
        perimeter = main.circumference(original_r)
        diameter = main.diameter(original_r)
        
        r_from_area = main.radius_from_area(area)
        r_from_perimeter = main.radius_from_perimeter(perimeter)
        r_from_diameter = main.radius_from_diameter(diameter)
        
        self.assertAlmostEqual(r_from_area, original_r, places=5)
        self.assertAlmostEqual(r_from_perimeter, original_r, places=5)
        self.assertAlmostEqual(r_from_diameter, original_r, places=5)

    def test_quarter_circle_perimeter_accuracy(self):
        # Test quarter circle perimeter formula
        r = 4
        quarter_perim = main.quarter_circle_perimeter(r)
        # Should be (πr/2) + 2r = πr/2 + 2r
        expected = (math.pi * r / 2) + (2 * r)
        self.assertAlmostEqual(quarter_perim, expected, places=5)

    def test_cube_surface_area_relations(self):
        # Test relationships between cube calculations
        side = 5
        full_surface = main.surface_area_cube(side)
        open_surface = main.surface_area_open_cube(side)
        half_surface = main.half_surface_area_cube(side)
        
        self.assertEqual(open_surface, full_surface - side ** 2)
        self.assertEqual(half_surface, full_surface / 2)

    def test_cylinder_volume_fractions(self):
        # Test fractional cylinder volumes
        r, h = 4, 6
        full_vol = main.volume_cylinder(r, h)
        half_vol = main.half_volume_cylinder(r, h)
        third_vol = main.third_volume_cylinder(r, h)
        
        self.assertAlmostEqual(half_vol, full_vol / 2, places=5)
        self.assertAlmostEqual(third_vol, full_vol / 3, places=5)

    def test_triangle_equilateral_with_circle_diameter(self):
        # Use triangle side as circle diameter
        triangle_side = 6
        triangle_result = triangle.triangle_type(triangle_side, triangle_side, triangle_side)
        radius = triangle_side / 2
        circle_area = main.area_of_circle(radius)
        
        self.assertIn("Equilateral", triangle_result)
        self.assertAlmostEqual(circle_area, math.pi * 9, places=5)

    def test_circle_area_triangle_perimeter_concept(self):
        # Calculate circle area and triangle type with related dimensions
        circle_radius = 5
        circle_area = main.area_of_circle(circle_radius)
        # Use radius as triangle sides
        triangle_result = triangle.triangle_type(
            int(circle_radius), int(circle_radius), int(circle_radius)
        )
        self.assertGreater(circle_area, 0)
        self.assertIn("Equilateral", triangle_result)

    def test_square_and_cube_relationship(self):
        # Test square area and cube volume with same side length
        side = 4
        square_area = main.area_square(side)
        cube_volume = main.volume_cube(side)
        # Square area should be side^2, cube volume should be side^3
        self.assertEqual(square_area, 16)
        self.assertEqual(cube_volume, 64)
        self.assertEqual(cube_volume, square_area * side)

    def test_semicircle_quarter_circle_relationship(self):
        # Test that semicircle is twice quarter circle area
        r = 8
        quarter_area = main.area_of_quarter_circle(r)
        semicircle_area = main.area_of_semicircle(r)
        self.assertAlmostEqual(semicircle_area, quarter_area * 2, places=5)

    def test_circle_perimeter_chain(self):
        # Chain of circle perimeter calculations
        r = 7
        circumference = main.circumference(r)
        semicircle_perim = main.semicircle_perimeter(r)
        quarter_perim = main.quarter_circle_perimeter(r)
        
        # All should be positive and related
        self.assertGreater(circumference, 0)
        self.assertGreater(semicircle_perim, 0)
        self.assertGreater(quarter_perim, 0)
        self.assertGreater(circumference, semicircle_perim)
        self.assertGreater(semicircle_perim, quarter_perim)

    def test_triangle_all_types_with_geometry(self):
        # Test all triangle types with geometry calculations
        # Equilateral
        eq_triangle = triangle.triangle_type(5, 5, 5)
        eq_circle = main.area_of_circle(5)
        
        # Isosceles
        iso_triangle = triangle.triangle_type(5, 5, 3)
        iso_circle = main.area_of_circle(5)
        
        # Scalene
        sca_triangle = triangle.triangle_type(3, 4, 5)
        sca_circle = main.area_of_circle(3)
        
        self.assertIn("Equilateral", eq_triangle)
        self.assertIn("Isosceles", iso_triangle)
        self.assertIn("Scalene", sca_triangle)
        self.assertGreater(eq_circle, 0)
        self.assertGreater(iso_circle, 0)
        self.assertGreater(sca_circle, 0)

    def test_cylinder_surface_area_open_closed_relation(self):
        # Test open cylinder surface area
        r, h = 5, 10
        open_cyl_area = main.surface_area_open_cylinder(r, h)
        # Open cylinder: 1 base + lateral = πr² + 2πrh
        expected = math.pi * r ** 2 + 2 * math.pi * r * h
        self.assertAlmostEqual(open_cyl_area, expected, places=5)

    def test_radius_diameter_consistency_integrated(self):
        # Test radius-diameter consistency across calculations
        r = 5
        d = main.diameter(r)
        r_calculated = main.radius_from_diameter(d)
        circle_area = main.area_of_circle(r)
        
        self.assertEqual(r_calculated, r)
        self.assertAlmostEqual(circle_area, math.pi * r ** 2, places=5)

    def test_volume_and_surface_area_cube_consistency(self):
        # Test cube volume and surface area consistency
        side = 3
        volume = main.volume_cube(side)
        surface_area = main.surface_area_cube(side)
        # Volume = side³, Surface = 6 * side²
        self.assertEqual(volume, 27)
        self.assertEqual(surface_area, 54)

    def test_error_handling_triangle_with_valid_geometry(self):
        # Test triangle error handling doesn't affect geometry
        invalid_triangle = triangle.triangle_type(0, 4, 5)
        valid_circle = main.area_of_circle(5)
        
        self.assertIn("Error", invalid_triangle)
        self.assertGreater(valid_circle, 0)

    def test_large_number_handling_integrated(self):
        # Test both programs handle large numbers
        large_r = 10000
        large_triangle_side = 10000
        
        circle_area = main.area_of_circle(large_r)
        triangle_result = triangle.triangle_type(
            large_triangle_side, large_triangle_side, large_triangle_side
        )
        
        self.assertGreater(circle_area, 0)
        self.assertIn("Equilateral", triangle_result)


if __name__ == '__main__':
    unittest.main()
