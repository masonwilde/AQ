# Name: Mason Wilde
# KUID: 2645990
# Course: EECS 690
# Professor: Dr Jerzy Gryzmala-Busse
# Semester: Fall 2017
# Project: AQ Rule Inducer
# File: dataset_test.py
# Date Modified:  2017-11-19
"""Test suite for dataset"""

import unittest
import dataset
from lers_reader import Lers_Reader

reader = Lers_Reader("datasets/numerical.txt")
mock_dataset = reader.read()


class TestDataset(unittest.TestCase):
    def test_attribute_is_discretizable_true(self):
        self.assertTrue(dataset.attribute_is_discretizable('Temperature', mock_dataset))
    def test_attribute_is_discretizable_false(self):
        self.assertFalse(dataset.attribute_is_discretizable('Headache', mock_dataset))
    def test_get_sorted_numerical_attribute_values(self):
        result = dataset.get_sorted_numerical_attribute_values("Temperature", mock_dataset)
        self.assertEqual(result, [70,80,90])
    def test_get_cutpoints(self):
        result = dataset.get_cutpoints([70,80,90])
        self.assertEqual(result, [75,85])
    def test_new_attr_name(self):
        result = dataset.new_attribute_name("Wind", 5)
        self.assertEqual(result, "Wind_5")
    def test_new_attr_name_float(self):
        result = dataset.new_attribute_name("Wind", 5.5)
        self.assertEqual(result, "Wind_5.5")

if __name__ == '__main__':
    unittest.main()
