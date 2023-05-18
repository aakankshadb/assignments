import unittest
from python_assignments.python_2_percentage_prob.core.utils import *
class MyTestCase(unittest.TestCase):
    def test_something(self):
        actualinput = percent_calc({'s1': [90, 90, 90], 's2': [10, 60, 250]}, 's1')
        expectedoutput = 90
        self.assertEqual(actualinput, format(expectedoutput,'.2f'))  # add assertion here


if __name__ == '__main__':
    unittest.main()
