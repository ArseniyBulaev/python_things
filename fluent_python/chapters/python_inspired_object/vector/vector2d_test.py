import unittest
from vector2d import Vector2D # type: ignore


class TestVector2D(unittest.TestCase):

    def test_zero_vector_is_false(self):
        self.assertFalse(Vector2D())
        
    def test_unpacking(self):
        v = Vector2D(3, 4)
        x, y = v
        coordinates = x, y
        self.assertEqual((3,4), coordinates)

    def test_wrong_construction(self):
        with self.assertRaises(ValueError):
            v = Vector2D("3ba", "4")

    def test_repr(self):
        v = Vector2D(3, 4)
        self.assertEqual("Vector2D(3.0, 4.0)", repr(v))

    def test_str(self):
        v = Vector2D(3, 4)
        self.assertEqual('(3.0, 4.0)', str(v))

    def test_abs(self):
        self.assertEqual(5, abs(Vector2D(3, 4)))
    
    def test_format(self):
        v = Vector2D(3, 4)
        v11 = Vector2D(1, 1)
        self.assertEqual(format(v), '(3.0, 4.0)')
        self.assertEqual(format(v, '.3f'), '(3.000, 4.000)')
        self.assertEqual(format(v, '.3e'), '(3.000e+00, 4.000e+00)')
        self.assertEqual(format(v11, 'p'), '<1.4142135623730951, 0.7853981633974483>')
        self.assertEqual(format(v11, '.3ep'), '<1.414e+00, 7.854e-01>')
        self.assertEqual(format(v11, '0.5fp'), '<1.41421, 0.78540>')
    
    def test_complex(self):
        v = Vector2D(1, 1)
        self.assertEqual(complex(v), 1+1j)

if __name__ == "__main__":
    unittest.main()