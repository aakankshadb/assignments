import unittest
from python_assignments.python_3_secondmax_prob.core.utils import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        actualoutput=second_max(5,[2,3,6,5,8])
        expectedoutput=6
        self.assertEqual(actualoutput, expectedoutput)  # add assertion here


if __name__ == '__main__':
    unittest.main()
