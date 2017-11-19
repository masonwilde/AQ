# Name: Mason Wilde
# KUID: 2645990
# Course: EECS 690
# Professor: Dr Jerzy Gryzmala-Busse
# Semester: Fall 2017
# Project: AQ Rule Inducer
# File: rule_tools.py
# Date Modified: 2017-11-19

from ruleset import Rule, Condition, Decision

def rule_from_complex(complex1, n_decision):
    new_conditions = []
    for selector in complex1:
        new_conditions.append(Condition(attribute =selector[0], value=selector[1]))
    return Rule(conditions = new_conditions, decision=Decision(n_decision[0], n_decision[1]))
