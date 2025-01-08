from src import math
import unittest


class TestUtil(unittest.TestCase):
    def average(self, *args):
        total = math.sum(*args)
        return math.div(total, len(args))

    def test_math(self):
        self.assertEqual(self.average(1, 2, 3), 2)
        self.assertEqual(self.average(10, 20, 30), 20)
        self.assertEqual(self.average(1.5, 0, 21), 7.5)


if __name__ == '__main__':
    unittest.main()
