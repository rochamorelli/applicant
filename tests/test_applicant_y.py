import unittest
from applicant_y import straight_line

class test_straigth_line(unittest.TestCase):
    def test_integral(self):
        line = straight_line(1, -1, 0)
        self.assertEqual(line.integral(0, 2), 2)
        self.assertEqual(line.integral(-2, 0), -2)
        self.assertEqual(line.integral(2, 4), 6)
        self.assertEqual(line.integral(-4, -2), -6)

        line = straight_line(3, -1, -6)
        self.assertEqual(line.integral(2, 3), 1.5)
        self.assertEqual(line.integral(3, 4), 4.5)

if __name__ == "__main__":
    unittest.main()
