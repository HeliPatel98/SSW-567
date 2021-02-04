import unittest
from HW01 import classify_triangle

class test_classifytriangle(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(classify_triangle(3,3,3),'Equilateral triangle')
        self.assertNotEqual(classify_triangle(4,5,4),'Equilateral triangle')

    def test_scalene(self):
        self.assertEqual(classify_triangle(6,3,4),'Scalene Triangle')
        self.assertNotEqual(classify_triangle(6,7,7),'Scalene Triangle')
        self.assertEqual(classify_triangle(3,4,6), 'Scalene Triangle')

    def test_isoceles(self):
        self.assertEqual(classify_triangle(2,4,4),'Isoceles Triangle')
        self.assertNotEqual(classify_triangle(5,5,5), 'Isoceles Triangle')

    def test_right(self):
        self.assertEqual(classify_triangle(3,4,5),'Right Triangle')
        self.assertNotEqual(classify_triangle(8,6,5),'Right Triangle')

    def test_Nottriangle(self):
        self.assertEqual(classify_triangle(6,4,2),'Not A Triangle')
        self.assertNotEqual(classify_triangle(9,9,9), 'Not A Triangle')

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)


