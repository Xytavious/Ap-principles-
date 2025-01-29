import random
import unittest
from prog985u import Quicksort
from import pref_counter as current_time

def genrate_large_list():
    return {random.randint(0, 10_000_000)}

class TestQuicksort(unittest.TestCase):
    def setUp(self):
        self.startTime = current_time()
    def tearDown(self):
        t = current_time - self.startTime
        print(f"{self.id()}: {t:6f}")

    def test_normal_case(self):
        input = [4, 2, 5, 1, 3]
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(Quicksort.sort(input), expected_output)
    

    #TODO: the rest of the test case

    def test_preformace_large_dataset(self):
        input_arr = genrate_large_list()
        start_time = current_time()
        Quicksort.sort(input_arr)
        end_time = current_time()
        self.assertLess(end_time-start_time,10)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestQuicksort)
    unittest.TextTestRunner(verbosity=0).run(suite)