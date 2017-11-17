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
