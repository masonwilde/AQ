#!/usr/bin/env python

# Name: Mason Wilde
# KUID: 2645990
# Course: EECS 690
# Professor: Dr Jerzy Gryzmala-Busse
# Semester: Fall 2017
# Project: AQ Rule Inducer
# File: verify_rules.py
# Date Modified: 2017-11-19
"""Tool to verify a ruleset for a dataset"""
import sys
import ruleset
from lers_reader import Lers_Reader

def main():
    checks=False
    if len(sys.argv)>2:
        dataset_filename=sys.argv[1]
        ruleset_filename=sys.argv[2]
        try:
            file_test = open(dataset_filename, 'r')
        except IOError:
            print "Dataset file could not be opened"
        try:
            file_test = open(ruleset_filename, 'r')
        except IOError:
            print "Ruleset file could not be opened"
        without=False
        if len(sys.argv)>3:
            if sys.argv[3] == "without":
                without = True
        the_rules = ruleset.read_rules(ruleset_filename)
        reader = Lers_Reader(dataset_filename)
        the_data = reader.read_improved()
        the_data.discretize()
        print "Ruleset is consistent:", the_rules.is_consistent(the_data, not without)
        print "Ruleset is complete:", the_rules.is_complete(the_data, not without)
    else:
        print "verify_rules.py <dataset_filename> <ruleset_filename> [without]"


if __name__ == "__main__":
    main()
