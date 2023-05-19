import unittest
from python_assignments.mutations_prob.core.utils import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        actualoutput=mutate_string('Timmy',0,'S')
        expectedoutput='Simmy'
        self.assertEqual(actualoutput,expectedoutput)  # add assertion here


if __name__ == '__main__':
    unittest.main()
