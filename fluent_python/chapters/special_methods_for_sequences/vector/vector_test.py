import unittest
from vector import Vector #type: ignore


class TestVector(unittest.TestCase):

    def test_zero_vector_is_false(self):
        self.assertFalse(abs(Vector([])))

    def test_repr(self):
        self.assertEqual(repr(Vector((3,4,5))), 'Vector([3.0, 4.0, 5.0])')

    def test_abs(self):
        self.assertEqual(abs(Vector([2,2,1])), 3)

    def test_str(self):
        self.assertEqual(str(Vector([3,4,5])), '(3.0, 4.0, 5.0)')

    def test_iter(self):
        v = Vector([3,4,5])
        x, y, z = v
        self.assertEqual(x, 3)
        self.assertEqual(y, 4)
        self.assertEqual(z, 5)

    def test_getitem(self):
        v = Vector([3,4,5])
        self.assertEqual(v[1], 4)
        self.assertEqual(v[1:], Vector([4, 5]))
        self.assertEqual(v[-3], 3)

    def test_len(self):
        v = Vector([1,2,3,4,5])
        self.assertEqual(len(v), 5)

    def test_from_bytes(self):
        v = Vector([3,4])
        v_copy = Vector.frombytes(bytes(v))
        self.assertEqual(v, v_copy)

    



if __name__ == "__main__":
    unittest.main()