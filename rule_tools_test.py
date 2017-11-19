# Name: Mason Wilde
# KUID: 2645990
# Course: EECS 690
# Professor: Dr Jerzy Gryzmala-Busse
# Semester: Fall 2017
# Project: AQ Rule Inducer
# File: rule_tools_test.py
# Date Modified: 2017-11-19

import unittest
import rule_tools
from lers_reader import Lers_Reader
from ruleset import Rule, Condition, Decision

reader = Lers_Reader("datasets/simple.txt")
mock_dataset = reader.read()

class TestRuleTools(unittest.TestCase):
    def test_rule_from_complex_single_selector(self):
        result = rule_tools.rule_from_complex([["Temperature", "high"]], ["Flue", "no"]).to_string()
        self.assertEqual(result, "(Temperature, not high) -> (Flue, no)")

    def test_rule_from_complex_multi_selector(self):
        result = rule_tools.rule_from_complex([["Temperature", "high"], ["Headache", "no"]], ["Flue", "no"]).to_string()
        self.assertEqual(result, "(Temperature, not high) & (Headache, not no) -> (Flue, no)")




if __name__ == '__main__':
    unittest.main()
