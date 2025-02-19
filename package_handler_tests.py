import unittest
from package_handler import (
    BULKY_DIMENSION_THRESHOLD,
    HEAVY_MASS_THRESHOLD,
    sort
)

class TestSort(unittest.TestCase):
    def test_standard_package(self):
        width, height, length, mass = BULKY_DIMENSION_THRESHOLD - 0.1, 10, 10, HEAVY_MASS_THRESHOLD - 0.1
        self.assertEqual(sort(width, height, length, mass), 'STANDARD')
        
    def test_bulky_by_volume(self):
        width, height, length, mass = 100, 100, 100, 5
        self.assertEqual(sort(width, height, length, mass), 'SPECIAL')
        
    def test_bulky_by_dimension(self):
        width, height, length, mass = BULKY_DIMENSION_THRESHOLD, 10, 10, 5
        self.assertEqual(sort(width, height, length, mass), 'SPECIAL')
        
    def test_heavy_package(self):
        width, height, length, mass = 10, 10, 10, HEAVY_MASS_THRESHOLD
        self.assertEqual(sort(width, height, length, mass), 'SPECIAL')
        
    def test_heavy_and_bulky_package(self):
        width, height, length, mass = BULKY_DIMENSION_THRESHOLD, 100, 100, HEAVY_MASS_THRESHOLD
        self.assertEqual(sort(width, height, length, mass), 'REJECTED')
        
    def test_invalid_dimensions(self):
        width, height, length, mass = -10, 10, 10, 5
        self.assertEqual(sort(width, height, length, mass), 'REJECTED')
        width = 0
        self.assertEqual(sort(width, height, length, mass), 'REJECTED')
        width = 'string'
        self.assertEqual(sort(width, height, length, mass), 'REJECTED')
        
    def test_invalid_mass(self):
        width, height, length, mass = 10, 10, 10, -5
        self.assertEqual(sort(width, height, length, mass), 'REJECTED')
        mass = 0
        self.assertEqual(sort(width, height, length, mass), 'REJECTED')
        mass = True
        self.assertEqual(sort(width, height, length, mass), 'REJECTED')


if __name__ == '__main__':
    unittest.main()