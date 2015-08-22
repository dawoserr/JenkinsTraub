__author__ = 'Jervis Muindi'

import unittest
from poly import *

class MyTestCase(unittest.TestCase):

    sample_poly = [2, -11, 17, -6]
    sample_poly_pow = 3

    sample_poly_2 = [6, -13, 7]
    sample_poly_pow_2 = 2

    sample_poly_3 = [1, -11, 17, -6]
    sample_poly_pow_3 = 3

    # The homework polynomial
    # It's a polynomial with the following roots:
    # 1-i ; 1+i ; 1 ; 1.01 ; 5
    # 'i' is the symbol for imaginary number
    # When expanded I got the following polynomial:
    # x^5 - 9.01*x^4 + (27.08)*x^3 -(41.19)*x^2 + (32.22)*x +  - 10.1
    hw_poly = [1, -9.01, 27.08, -41.19, 32.22, -10.1]
    hw_poly_pow = 5



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

    def test_poly_eq(self):
        p1 = Poly(self.sample_poly_pow, self.sample_poly)
        p2 = Poly(self.sample_poly_pow, self.sample_poly)
        p3 = Poly(self.sample_poly_pow_2, self.sample_poly_2)
        self.assertTrue(p1 == p2)
        self.assertFalse(p1 == p3)

    def test_poly_eval(self):
        p = Poly(self.sample_poly_pow, self.sample_poly)

        actual = p.eval(0)
        expected = -6
        self.assertEqual(actual, expected)

        #Test a some random number
        actual = p.eval(17)
        expected = 6930
        self.assertEqual(actual, expected)


    def test_poly_get_power_at_index(self):
        p = Poly(self.sample_poly_pow, self.sample_poly)

        max_deg = p.highest_degree()
        cur_deg = max_deg
        index = 0
        for c in p.coeff:
            actual = p.get_power_at_index(index)
            expected = cur_deg
            self.assertEqual(actual, expected)
            index += 1
            cur_deg -= 1

    def test_poly_get_derivative(self):
        p = Poly(self.sample_poly_pow, self.sample_poly)

        expected_ans = [6, -22, 17]
        expected = Poly(p.highest_degree() - 1, expected_ans)
        actual = p.get_derivative()

        self.assertTrue(expected == actual)


    def test_poly_const_mult(self):
        p = Poly(self.sample_poly_pow, self.sample_poly)
        multipler = 7
        expected_coeff = map(lambda x: multipler*x, self.sample_poly)
        expected = Poly(p.highest_degree(), expected_coeff)
        actual = p.const_mult(multipler)

        self.assertTrue(expected == actual)

    def test_poly_negate(self):
        p = Poly(self.sample_poly_pow, self.sample_poly)

        expected_coeff = map(lambda x: -x, self.sample_poly)
        expected = Poly(p.highest_degree(), expected_coeff)
        actual = p.negate()
        self.assertTrue(expected == actual)

    def test_poly_subtraction(self):
        p1 = Poly(self.sample_poly_pow, self.sample_poly)
        p2 = Poly(self.sample_poly_pow_2, self.sample_poly_2)

        expected_ans = [2, -17, 30, -13]
        ans  = p1 - p2

        self.assertTrue(ans.size() == len(expected_ans))
        for i in xrange(ans.size()):
            self.assertEqual(ans.coeff[i], expected_ans[i])


    def test_get_empty_poly(self):
        expected_coeff = [0, 0, 0, 0]
        expected_pow = 3
        expected = Poly(expected_pow, expected_coeff)
        actual = get_empty_poly(3)
        self.assertTrue(actual == expected)

    def test_poly_set_coeff_at_x_power(self):
        expected_coeff = [6, -3, 0, 7]
        expected_pow = 3
        expected = Poly(expected_pow, expected_coeff)

        p = get_empty_poly(3)
        p.set_coeff_at_x_power(0,7)
        p.set_coeff_at_x_power(1,0)
        p.set_coeff_at_x_power(2,-3)
        p.set_coeff_at_x_power(3,6)
        actual = p
        self.assertTrue(actual == expected)

    def test_term_multiply_linear_poly(self):

        t = Term(2,2)
        actual = t.multiply_linear_poly(1,-3)

        expected_coeff = [2,-6,0,0]
        expected_pow = len(expected_coeff) - 1

        expected = Poly(expected_pow, expected_coeff)

        self.assertTrue(actual == expected)

    def test_poly_get_highest_degree_of_non_zero_coeff(self):
        p = get_empty_poly(3)
        p.set_coeff_at_x_power(2,6)
        expected = 2
        actual = p.get_highest_degree_of_non_zero_coeff()
        self.assertEqual(expected, actual)

    def test_poly_divide_linear_poly(self):
        p = Poly(self.sample_poly_pow, self.sample_poly)
        actual = p.divide_linear_poly(1, -3)

        expected_coeff = [2, -5, 2]
        expected_pow = len(expected_coeff) - 1
        expected = Poly(expected_pow, expected_coeff)

        self.assertTrue(expected == actual)

        # Test non-perfect division example
        actual = p.divide_linear_poly(1,-4)
        expected_coeff = [2, -3, 5]
        expected_pow = len(expected_coeff) - 1
        expected = Poly(expected_pow, expected_coeff)
        self.assertTrue(expected == actual)

    def test_get_cauchy_poly(self):
        p = Poly(self.sample_poly_pow, self.sample_poly)
        actual = p.get_cauchy_poly()

        expected_coeff = [1, 5.5, 8.5, -3]

        expected_pow = len(expected_coeff) - 1
        expected = Poly(expected_pow, expected_coeff)

        self.assertTrue(expected == actual)

    def test_solve_poly_newton(self):
        p = Poly(self.sample_poly_pow, self.sample_poly)
        err = 10 ** -6
        cauchy_poly = p.get_cauchy_poly()
        actual = solve_poly_newton(cauchy_poly, err)
        expected = 0.294016

        self.assertAlmostEquals(actual, expected, delta=err)



    def test_get_initial_s(self):
        p = Poly(self.sample_poly_pow, self.sample_poly)
        actual = get_initial_s(p)
        actual_abs = abs(actual)
        expected = 0.294016
        err = 10 ** (-4)

        self.assertAlmostEquals(actual_abs, expected, delta=err)

    def test_poly_normalize(self):
        p = Poly(self.sample_poly_pow, self.sample_poly)
        actual = p.normalize()
        expected_coeff = [1, -5.5, 8.5, -3]

        expected_pow = len(expected_coeff) - 1
        expected = Poly(expected_pow, expected_coeff)

        self.assertTrue(expected == actual)


    def test_solve_smallest_root_poly_jt(self):
        err = 10 ** (-5)
        p = Poly(self.sample_poly_pow, self.sample_poly)

        actual = solve_smallest_root_poly_jt(p, err)
        actual = abs(actual)
        expected = 0.5

        self.assertAlmostEqual(actual,expected,delta=err)

    def test_solve_all_roots_poly_jt(self):
        err = 10 ** (-5)
        p = Poly(self.sample_poly_pow, self.sample_poly)

        actual_roots = solve_poly_jt(p, err)
        expected_roots = [0.5, 2, 3]

        for i in xrange(len(expected_roots)):
            expected = expected_roots[i]
            actual = abs(actual_roots[i])
            self.assertAlmostEqual(actual,expected,delta=err)

    def test_solve_all_root_homewrok(self):
        """
            Test Finding all the roots for the Homework Polynomial
        """
        err = 10 ** (-5)
        p = Poly(self.hw_poly_pow, self.hw_poly)

        actual_roots = solve_poly_jt(p, err)
        expected_roots = [1, 1.01, complex(1,-1), complex(1,1), 5]

        print actual_roots

        # Use Big Delta b'se of the two close roots 1 and 1.01
        delta = 5 * 10 ** (-2)
        delta_comp = 5 * 10 ** (-2)
        for i in xrange(len(expected_roots)):
            expected = expected_roots[i]
            actual = actual_roots[i]
            self.assertAlmostEqual(abs(actual),abs(expected),delta=delta)
            self.assertAlmostEqual(abs(actual.real),abs(expected.real),delta=delta_comp)
            self.assertAlmostEqual(abs(actual.imag),abs(expected.imag),delta=delta_comp)


    def test_solve_quartic_poly(self):
        """
            Test Finding a quartic polynomial. 
        """
        err = 10 ** (-5)
        poly_pow = 4
        input_poly = [1, 0, -1, 0, 0.125]
        p = Poly(poly_pow, input_poly)

        actual_roots = solve_poly_jt(p, err)
        expected_roots = [-0.3826, 0.3826, -0.92388, 0.92388]

        print actual_roots

        # Use Big Delta as roots as far apart.
        delta = 5 * 10 ** (-2)
        delta_comp = 5 * 10 ** (-2)
        for i in xrange(len(expected_roots)):
            expected = expected_roots[i]
            actual = actual_roots[i]
            
            self.assertAlmostEqual(abs(actual),abs(expected),delta=delta)
            self.assertAlmostEqual(abs(actual.real),abs(expected.real),delta=delta_comp)
            self.assertAlmostEqual(abs(actual.imag),abs(expected.imag),delta=delta_comp)


    def test_solve_simple_complex_poly(self):
        """
            Regression test on finding complex roots for a simple polynomial: x^2 + 1 = 0.
        """
        err = 10 ** (-3)
        poly_pow = 2
        input_poly = [1, 0, 1]
        p = Poly(poly_pow, input_poly)

        actual_roots = solve_poly_jt(p, err)
        expected_roots = [0+1j, 0-1j]

        print actual_roots

        # Use same comparison delta as |err| given to solve_poly_gt()
        delta = err
        delta_complex = err
        for i in xrange(len(expected_roots)):
            expected = expected_roots[i]
            actual = actual_roots[i]

            self.assertAlmostEqual(abs(actual),abs(expected),delta=delta)
            self.assertAlmostEqual(abs(actual.real),abs(expected.real),delta=delta_complex)
            self.assertAlmostEqual(abs(actual.imag),abs(expected.imag),delta=delta_complex)


if __name__ == '__main__':
    unittest.main()
