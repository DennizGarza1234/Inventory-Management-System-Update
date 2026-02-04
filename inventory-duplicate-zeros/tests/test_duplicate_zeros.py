# pylint: disable=import-error, wrong-import-position

import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from duplicate_zeros import duplicateZeros

class TestDuplicateZeros(unittest.TestCase):

    def test_normal_case_1(self):
        inventory = [4, 0, 1, 3, 0, 2, 5, 0]
        duplicateZeros(inventory)
        self.assertEqual(inventory, [4, 0, 0, 1, 3, 0, 0, 2])

    def test_normal_case_2(self):
        inventory = [1, 0, 2, 3, 0, 4, 5, 0]
        duplicateZeros(inventory)
        self.assertEqual(inventory, [1, 0, 0, 2, 3, 0, 0, 4])

    def test_normal_case_3(self):
        inventory = [0, 1, 2, 3]
        duplicateZeros(inventory)
        self.assertEqual(inventory, [0, 0, 1, 2])


    def test_no_zeros(self):
        inventory = [3, 2, 1]
        duplicateZeros(inventory)
        self.assertEqual(inventory, [3, 2, 1])

    def test_all_zeros(self):
        inventory = [0, 0, 0]
        duplicateZeros(inventory)
        self.assertEqual(inventory, [0, 0, 0])

    def test_single_element(self):
        inventory = [0]
        duplicateZeros(inventory)
        self.assertEqual(inventory, [0])


if __name__ == "__main__":
    unittest.main()
