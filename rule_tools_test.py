import unittest
import rule_tools
from lers_reader import Lers_Reader
from ruleset import Rule, Condition, Decision

reader = Lers_Reader("simple_consistent.d")
mock_dataset = reader.read()

class TestRuleTools(unittest.TestCase):
    def test_rule_from_complex_single_selector(self):
        result = rule_tools.rule_from_complex([["Temperature", "high"]], ["Flue", "no"]).to_string()
        self.assertEqual(result, "(Temperature, not high) -> (Flue, no)")

    def test_rule_from_complex_multi_selector(self):
        result = rule_tools.rule_from_complex([["Temperature", "high"], ["Headache", "no"]], ["Flue", "no"]).to_string()
        self.assertEqual(result, "(Temperature, not high) & (Headache, not no) -> (Flue, no)")

    def test_get_available_attribute_values(self):
        rule = Rule(conditions=[Condition(attribute="Temperature", value="very_high")], decision=Decision(label="Flue", value="no"))
        result = rule_tools.get_available_attribute_values(mock_dataset, rule)
        self.assertEqual(result, {"Temperature":["high", "normal"]})

if __name__ == '__main__':
    unittest.main()
