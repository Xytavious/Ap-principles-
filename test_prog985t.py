import random
import unittest
from prog985t import mergesort
from time import perf_counter as current_time


def generate_large_list():
    return [random.randint(0, 10_000_000) for i in range(1_000_000)]


class TestMergeSort(unittest.TestCase):
    def setUp(self):
        self.startTime = current_time()

    def tearDown(self):
        t = current_time() - self.startTime
        print(f"{self.id()}: {t:6f}")

    def test_normal_case(self):
        input_arr = [4, 2, 5, 1, 3]
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(mergesort.sort(input_arr), expected_output)

    def test_ident_case(self):
        input_arr = [4, 4, 4, 4, 4]
        expected_output = [4, 4, 4, 4, 4]
        self.assertEqual(mergesort.sort(input_arr), expected_output)

    def test_neg_case(self):
        input_arr = [-4, -2, -10, -21, -3]
        expected_output = [-21, -10, -4, -3, -2]
        self.assertEqual(mergesort.sort(input_arr), expected_output) 

    def test_mixed_case(self):
        input_arr = [4.5, -2, 5, 1, 3.2]
        expected_output = [-2, 1, 3.2, 4.5, 5]
        self.assertEqual(mergesort.sort(input_arr), expected_output)

    def test_empty_case(self):
        input_arr = [0, 0, 0, 0, 0]
        expected_output = [0, 0, 0, 0, 0]
        self.assertEqual(mergesort.sort(input_arr), expected_output)

    def test_performance_large_dataset(self):
        input_arr = generate_large_list()
        start_time = current_time()
        mergesort.sort(input_arr)
        end_time = current_time()
        self.assertLess(end_time-start_time, 10)

    def test_single_case(self):
        input_arr = [4]
        expected_output = [4]
        self.assertEqual(mergesort.sort(input_arr), expected_output)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMergeSort)
    unittest.TextTestRunner(verbosity=0).run(suite)