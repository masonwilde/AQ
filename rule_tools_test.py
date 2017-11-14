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

    def test_expand_ruleset_simple(self):
        result = rule_tools.expand_ruleset(
                            [Rule(conditions=[],
                                    decision=Decision(label="Flue", value="yes"))],
                            "Temp", ["high", "normal"])
        expected_ruleset = [Rule(conditions=[Condition(attribute="Temp", value="high")],
                                decision=Decision(label="Flue", value="yes")),
                            Rule(conditions=[Condition(attribute="Temp", value="normal")],
                                decision=Decision(label="Flue", value="yes"))]
        for i in range(len(expected_ruleset)):
            for j in range(len(expected_ruleset[i].conditions)):
                self.assertEqual(expected_ruleset[i].conditions[j], result[i].conditions[j])

    def test_unnegate_rule(self):
        rule = Rule(conditions=[Condition(attribute="Temperature", value="very_high"),
                                Condition(attribute="Headache", value="no")],
                    decision=Decision(label="Flue", value="no"))
        result = rule_tools.unnegate_rule(mock_dataset, rule)
        expected_ruleset = [Rule(conditions=[Condition(attribute="Temperature", value="high"), Condition(attribute="Headache", value="yes")],
                                decision=Decision(label="Flue", value="yes")),
                            Rule(conditions=[Condition(attribute="Temperature", value="normal"), Condition(attribute="Headache", value="yes")],
                                decision=Decision(label="Flue", value="yes"))]
        for i in range(len(expected_ruleset)):
            for j in range(len(expected_ruleset[i].conditions)):
                self.assertEqual(expected_ruleset[i].conditions[j], result[i].conditions[j])

if __name__ == '__main__':
    unittest.main()
