# test_prog985a.py
import unittest
from  prog985a import Calc
from time import perf_counter as current_time
""" Test each case with the following:
Normal case: 1, 2
Edge case: 0, 0
Error case: 1, -1
"""


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.startTime = current_time()

    def tearDown(self):
        t = current_time() - self.startTime
        print(f"{self.id()}: {t:6f}")

    def test_add_normal_case(self):
        self.assertEqual(Calc.add(1, 2), 3)

    def test_add_edge_case(self):
        self.assertEqual(Calc.add(0, 0), 0)

    def test_add_error_case(self):
        self.assertEqual(Calc.add(1, -1), 0)

    # TODO: finish sub, mul, and mod

    def test_div_normal_case(self):
        self.assertEqual(Calc.div(1, 2), 0.5)

    def test_div_edge_case(self):
        with self.assertRaises(ZeroDivisionError):
            Calc.div(0, 0)

    def test_div_error_case(self):
        self.assertEqual(Calc.div(1, -1), -1)

    #weeee

    def test_sub_normal_case(self):
        self.assertEqual(Calc.sub(2, 1), 1)

    def test_sub_edge_case(self):
        with self.assertRaises((0, 0), 0):
            Calc.sub(0, 0)

    def test_sub_error_case(self):
        self.assertEqual(Calc.sub(1, -1), -1)

    #yyyyy

    def test_mul_normal_case(self):
        self.assertEqual(Calc.mul(1, 2), 2)

    def test_mul_edge_case(self):
        self.assertEqual(Calc.mul(0, 0), 0)

    def test_mul_error_case(self):
        self.assertEqual(Calc.mul(1, -1), 0)


    #MMMMMMMM

    def test_mod_normal_case(self):
        self.assertEqual(Calc.mod(5, 2), 1)

    def test_mod_edge_case(self):
        with self.assertRaises(ZeroDivisionError):
            Calc.mod(0, 0)

    def test_mod_error_case(self):
        self.assertEqual(Calc.mod(1, -1), -1)


if __name__ == '__main__':
    # Run w/ either "python test_prog985a.py" or "python -m unittest test_prog985a.py"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalc)
    unittest.TextTestRunner(verbosity=0).run(suite)