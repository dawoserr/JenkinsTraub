__author__ = 'Jervis Muindi'

import unittest
from poly import *

class MyTestCase(unittest.TestCase):

    sample_poly = [2, -11, 17, -6]
    sample_poly_pow = 3

    sample_poly_2 = [6, -13, 7]
    sample_poly_pow_2 = 2




    def test_poly_init(self):

        poly_size = len(self.sample_poly)
        p = Poly(self.sample_poly_pow, self.sample_poly)

        for i in xrange(poly_size):
            self.assertEqual(self.sample_poly[i], p.coeff[i])


    def test_poly_add(self):
        p1 = Poly(self.sample_poly_pow, self.sample_poly)
        p2 = Poly(self.sample_poly_pow_2, self.sample_poly_2)

        expected_ans = [2, -5, 4, 1]
        ans  = p1 + p2

        self.assertTrue(ans.size() == len(expected_ans))
        for i in xrange(ans.size()):
            self.assertEqual(ans.coeff[i], expected_ans[i])

if __name__ == '__main__':
    unittest.main()
