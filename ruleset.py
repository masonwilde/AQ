# Name: Mason Wilde
# KUID: 2645990
# Course: EECS 690
# Professor: Dr Jerzy Gryzmala-Busse
# Semester: Fall 2017
# Project: AQ Rule Inducer
# File: ruleset.py
# Date Modified: 2017-11-19

import sys

def get_available_attribute_values(dataset, rule):
    attribute_values = {}
    for condition in rule.conditions:
        if condition.attribute not in attribute_values:
            attribute_values[condition.attribute] = dataset.attribute_value_ranges[condition.attribute]
        attribute_values[condition.attribute] = list(set(attribute_values[condition.attribute]) - set([condition.value]))
    return attribute_values

def expand_ruleset(ruleset, attr, values):
    new_ruleset = []
    for rule in ruleset:
        # print "Starting with Rule:", rule.to_string()
        starting_conditions = rule.conditions
        for val in values:
            # print "\tAdd rule with", attr, val
            new_rule = Rule(decision=rule.decision)
            # print "\trule to build on is", new_rule.to_string()
            new_rule.conditions = starting_conditions + [Condition(attribute=attr, value=val)]
            # print "\tappending", new_rule.to_string()
            new_ruleset.append(new_rule)
    return new_ruleset

def unnegate_rule(dataset, rule):
    available_attribute_values = get_available_attribute_values(dataset, rule)
    new_ruleset = [Rule(decision=rule.decision)]
    for attribute in available_attribute_values:
        new_ruleset = expand_ruleset(new_ruleset, attribute, available_attribute_values[attribute])
    return new_ruleset

def read_rules(filename):
    ruleset = Ruleset()
    rule_file = open(filename, 'r')
    blank_rule = Rule()
    for line in rule_file:
        new_rule = blank_rule
        conditions, arrow, decision = line.partition("->")
        decision = decision.replace("(", "").replace(")", "").strip()
        decision = decision.split(",")
        decision[0] = decision[0].strip()
        decision[1] = decision[1].strip()
        conditions = conditions.replace("(", "").replace(")", "").strip()
        conditions = conditions.split("&")
        conditions_list = []
        for condition in conditions:
            condition = condition.split(",")
            condition[1] = condition[1].replace("not", "").strip()
            condition = Condition(attribute=condition[0].strip(), value=condition[1].strip())
            conditions_list.append(condition)
        # print "new rule is", new_rule.to_string()
        ruleset.rules.append(Rule(conditions=conditions_list, decision=Decision(label=decision[0], value=decision[1])))
    # ruleset.display()
    return ruleset


class Condition(object):
    def __init__(self, attribute = None, value = None):
        self._attribute = attribute
        self._value = value

    def __eq__(self, other):
        return self.attribute == other.attribute and self.value == other.value

    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, value):
        self._attribute = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, n_value):
        self._value = n_value

class Decision(object):
    def __init__(self, label = None, value = None):
        self._label = label
        self._value = value

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, n_value):
        self._value = n_value

class Rule(object):
    def __init__(self, conditions =[], decision = None):
        self._conditions = conditions
        self._decision = decision

    @property
    def conditions(self):
        return self._conditions

    @conditions.setter
    def conditions(self, value):
        self._conditions = value

    @property
    def decision(self):
        return self._decision

    @decision.setter
    def decision(self, value):
        self._decision = value

    def to_string(self, negated=True):
        rule = ""
        for i, condition in enumerate(self.conditions):
            if i > 0:
                rule += "& "
            rule += "(" + condition.attribute + (", not " if negated else ", ") + condition.value + ") "
        rule += "-> (" + self.decision.label + ", " + self.decision.value + ")"
        return rule

    def covers(self, case, negated=True):
        for condition in self.conditions:
            if negated:
                if case.attribute_values[condition.attribute] == condition.value:
                    return False
            else:
                if case.attribute_values[condition.attribute] != condition.value:
                    return False
        return True

    def cases_covered(self, dataset, negated=True):
        covered = []
        for i, case in enumerate(dataset.universe):
            if(self.covers(case, negated)):
                covered.append(i)
        return covered


    def is_consistent(self, dataset, negated=True):
        for case in self.cases_covered(dataset, negated):
                if dataset.universe[case].decision != self.decision.value:
                    print "Rule is inconsistent"
                    print "\tRule:", self.to_string(negated)
                    print "\tCase: #", case
                    sys.stdout.write('\t')
                    for attribute in dataset.attributes:
                        sys.stdout.write(attribute + '\t')
                    sys.stdout.write(dataset.decision + '\n')
                    case = dataset.universe[case]
                    sys.stdout.write('\t')
                    for attribute in dataset.attributes:
                        sys.stdout.write(case.attribute_values[attribute] + '\t')
                    sys.stdout.write(case.decision + '\n')
                    return False
        return True

class Ruleset(object):
    def __init__(self, rules=[]):
        self._rules = rules

    @property
    def rules(self):
        return self._rules

    @rules.setter
    def rules(self, value):
        self._rules = value

    def display(self, negated=True):
        for rule in self.rules:
            print rule.to_string(negated)

    def print_to_file(self, filename, negated=True):
        f = open(filename, 'w')
        for rule in self.rules:
            f.write(rule.to_string(negated) + '\n')
        f.closed

    def unnegate(self, dataset):
        new_ruleset = []
        for rule in self.rules:
            new_ruleset = new_ruleset + unnegate_rule(dataset, rule)
        return new_ruleset

    def is_consistent(self, dataset, negated=True):
        for rule in self.rules:
            if not rule.is_consistent(dataset, negated):
                return False
        return True

    def is_complete(self, dataset, negated=True):
        covered = []
        for rule in self.rules:
            covered = list(set(covered).union(set(rule.cases_covered(dataset, negated))))
        return covered == range(len(dataset.universe))
