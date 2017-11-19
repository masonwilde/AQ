# Name: Mason Wilde
# KUID: 2645990
# Course: EECS 690
# Professor: Dr Jerzy Gryzmala-Busse
# Semester: Fall 2017
# Project: AQ Rule Inducer
# File: ruleset_test.py
# Date Modified: 2017-11-19

import unittest
import ruleset
from ruleset import Rule, Condition, Decision, Ruleset
from lers_reader import Lers_Reader

reader = Lers_Reader("datasets/simple.txt")
mock_dataset = reader.read_improved()

class TestRuleset(unittest.TestCase):
    def test_get_available_attribute_values(self):
        rule = Rule(conditions=[Condition(attribute="Temperature", value="very_high")], decision=Decision(label="Flue", value="no"))
        result = ruleset.get_available_attribute_values(mock_dataset, rule)
        self.assertEqual(result, {"Temperature":["high", "normal"]})

    def test_expand_ruleset_simple(self):
        result = ruleset.expand_ruleset(
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
        result = ruleset.unnegate_rule(mock_dataset, rule)
        expected_ruleset = [Rule(conditions=[Condition(attribute="Temperature", value="high"), Condition(attribute="Headache", value="yes")],
                                decision=Decision(label="Flue", value="yes")),
                            Rule(conditions=[Condition(attribute="Temperature", value="normal"), Condition(attribute="Headache", value="yes")],
                                decision=Decision(label="Flue", value="yes"))]
        for i in range(len(expected_ruleset)):
            for j in range(len(expected_ruleset[i].conditions)):
                self.assertEqual(expected_ruleset[i].conditions[j], result[i].conditions[j])

    def test_covered_cases_negated(self):
        rule = Rule(conditions=[Condition(attribute="Temperature", value="normal")],
                    decision=Decision(label="Flue", value="no"))
        self.assertEqual(rule.cases_covered(mock_dataset), [0,1,3,4])

    def test_covered_cases_unnegated(self):
        rule = Rule(conditions=[Condition(attribute="Temperature", value="normal")],
                    decision=Decision(label="Flue", value="no"))
        self.assertEqual(rule.cases_covered(mock_dataset, negated=False), [2,5,6])

    def test_rule_is_consistent_negated(self):
        rule = Rule(conditions=[Condition(attribute="Temperature", value="normal")],
                    decision=Decision(label="Flue", value="no"))
        self.assertFalse(rule.is_consistent(mock_dataset))

    def test_rule_is_consistent_unnegated(self):
        rule = Rule(conditions=[Condition(attribute="Temperature", value="normal")],
                    decision=Decision(label="Flue", value="no"))
        self.assertTrue(rule.is_consistent(mock_dataset, negated=False))

    def test_ruleset_is_consistent_negated_false(self):
        rule1 = Rule(conditions=[Condition(attribute="Temperature", value="normal")],
                    decision=Decision(label="Flue", value="yes"))
        rule2 = Rule(conditions=[Condition(attribute="Temperature", value="high")],
                    decision=Decision(label="Flue", value="no"))
        rule3 = Rule(conditions=[Condition(attribute="Temperature", value="very_high")],
                    decision=Decision(label="Flue", value="no"))
        ruleset = Ruleset(rules=[rule1,rule2,rule3])
        self.assertFalse(ruleset.is_consistent(mock_dataset))

    def test_ruleset_is_complete_negated_true(self):
        rule1 = Rule(conditions=[Condition(attribute="Temperature", value="normal"),
                    Condition(attribute="Headache", value="no")],
                    decision=Decision(label="Flue", value="yes"))
        rule2 = Rule(conditions=[Condition(attribute="Temperature", value="high"),
                    Condition(attribute="Temperature", value="very_high")],
                    decision=Decision(label="Flue", value="no"))
        rule3 = Rule(conditions=[Condition(attribute="Headache", value="yes")],
                    decision=Decision(label="Flue", value="no"))
        ruleset = Ruleset(rules=[rule1,rule2,rule3])
        self.assertTrue(ruleset.is_complete(mock_dataset))

    def test_ruleset_is_consistent_negated_true(self):
        rule1 = Rule(conditions=[Condition(attribute="Temperature", value="normal"),
                    Condition(attribute="Headache", value="no")],
                    decision=Decision(label="Flue", value="yes"))
        rule2 = Rule(conditions=[Condition(attribute="Temperature", value="high"),
                    Condition(attribute="Temperature", value="very_high")],
                    decision=Decision(label="Flue", value="no"))
        rule3 = Rule(conditions=[Condition(attribute="Headache", value="yes")],
                    decision=Decision(label="Flue", value="no"))
        ruleset = Ruleset(rules=[rule1,rule2,rule3])
        self.assertTrue(ruleset.is_consistent(mock_dataset))

    def test_ruleset_is_complete_negated_false(self):
        rule1 = Rule(conditions=[Condition(attribute="Temperature", value="normal"),
                    Condition(attribute="Headache", value="no")],
                    decision=Decision(label="Flue", value="yes"))
        ruleset = Ruleset(rules=[rule1])
        self.assertFalse(ruleset.is_complete(mock_dataset))

    def test_ruleset_is_complete_unnegated_false(self):
        rule1 = Rule(conditions=[Condition(attribute="Temperature", value="normal"),
                    Condition(attribute="Headache", value="no")],
                    decision=Decision(label="Flue", value="yes"))
        ruleset = Ruleset(rules=[rule1])
        self.assertFalse(ruleset.is_complete(mock_dataset, negated=False))

    def test_ruleset_is_consistent_unnegated_false(self):
        rule1 = Rule(conditions=[Condition(attribute="Temperature", value="normal"),
                    Condition(attribute="Headache", value="no")],
                    decision=Decision(label="Flue", value="yes"))
        rule2 = Rule(conditions=[Condition(attribute="Temperature", value="high"),
                    Condition(attribute="Temperature", value="very_high")],
                    decision=Decision(label="Flue", value="no"))
        rule3 = Rule(conditions=[Condition(attribute="Headache", value="yes")],
                    decision=Decision(label="Flue", value="no"))
        ruleset = Ruleset(rules=[rule1,rule2,rule3])
        self.assertFalse(ruleset.is_consistent(mock_dataset, negated=False))

if __name__ == '__main__':
    unittest.main()
