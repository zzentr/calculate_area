import unittest
from find_the_area import Circle, Triangle


class TestCircleArea(unittest.TestCase):

    def test_area(self):
        circ = Circle(5)
        self.assertEqual(circ.area(), 78.5)
        circ = Circle(1)
        self.assertEqual(circ.area(), 3.14)
        circ = Circle(10)
        self.assertEqual(circ.area(), 314)
        circ = Circle(5.3)
        self.assertEqual(circ.area(), 88.2026)

    def test_values(self):
        circ = Circle(-1)
        with self.assertRaises(ValueError):
            circ.area()

    def test_types(self):
        circ = Circle(4-2j)
        with self.assertRaises(TypeError):
            circ.area()
        circ = Circle('five')
        with self.assertRaises(TypeError):
            circ.area()
        circ = Circle([5, 'hello'])
        with self.assertRaises(TypeError):
            circ.area()


class TestTriangleArea(unittest.TestCase):

    def test_area(self):
        trian = Triangle(2, 3, 4)
        self.assertEqual(trian.area(), 2.905)
        trian = Triangle(5, 2, 6)
        self.assertEqual(trian.area(), 4.684)
        trian = Triangle(11, 5, 9)
        self.assertEqual(trian.area(), 22.185)

    def test_values(self):
        trian = Triangle(11, 2, 3)
        with self.assertRaises(ValueError):
            trian.area()
        trian = Triangle(5, 0, -1)
        with self.assertRaises(ValueError):
            trian.area()

    def test_types(self):
        trian = Triangle(2-5j, 2, 1)
        with self.assertRaises(TypeError):
            trian.area()
        trian = Triangle(2, "two", 0)
        with self.assertRaises(TypeError):
            trian.area()
        trian = Triangle([1, 3, 5], '5', (123))
        with self.assertRaises(TypeError):
            trian.area()