# Name: Mason Wilde
# KUID: 2645990
# Course: EECS 690
# Professor: Dr Jerzy Gryzmala-Busse
# Semester: Fall 2017
# Project: AQ Rule Inducer
# File: dataset.py
# Date Modified:  2017-11-19

import sys

def attribute_is_discretizable(attribute, dataset):
    """Returns true if the values for an attribute are numerical"""
    try:
        x = float(dataset.universe[0].attribute_values[attribute])
        return True
    except:
        return False

def get_sorted_numerical_attribute_values(attribute, dataset):
    """Returns a sorted list of all possible numerical values for an attribute"""
    vals = []
    for case in dataset.universe:
        numerical_val = float(case.attribute_values[attribute])
        if numerical_val not in vals:
            vals.append(numerical_val)
    return sorted(vals)

def get_cutpoints(vals):
    """Returns a list of cutpoints for a given attribute"""
    cutpoints = []
    for i in range(len(vals)-1):
        cutpoint = (vals[i]+vals[i+1])/2.0
        int_cutpoint = int(cutpoint)
        if int_cutpoint == cutpoint:
            cutpoint = int_cutpoint
        cutpoints.append(cutpoint)
    return cutpoints

def new_attribute_name(attribute, cutpoint):
    """Returns a new attribute name for a given cutpoint"""
    return "" + attribute + "_" + str(cutpoint)

def populate_discretized_attribute(dataset, init_attr, new_attr_name, cutpoint, min_val, max_val):
    """Fills in values for cases for new discretized attributes"""
    for case in dataset.universe:
        case_val = float(case.attribute_values[init_attr])
        if case_val < cutpoint:
            new_val = str(min_val) + ".." + str(cutpoint)
        else:
            new_val = str(cutpoint) + ".." + str(max_val)
        case.attribute_values[new_attr_name] = new_val

class Dataset(object):
    """A class to store a dataset"""

    def __init__(self):
        self._attributes = []
        self._decision = None
        self._universe = []
        self._attribute_value_ranges = {}
        self._decision_range = []
        self._symbolic = True
        self._consistent = True

    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, value):
        self._attributes = value

    @property
    def decision(self):
        return self._decision

    @decision.setter
    def decision(self, value):
        self._decision = value

    @property
    def universe(self):
        return self._universe

    @universe.setter
    def universe(self, value):
        self._universe = value

    def append_to_universe(self, value):
        self._universe.append(value)

    @property
    def attribute_value_ranges(self):
        return self._attribute_value_ranges

    @attribute_value_ranges.setter
    def attribute_ranges(self, value):
        self._attribute_value_ranges = value

    @property
    def decision_range(self):
        return self._decision_range

    @decision_range.setter
    def decision_range(self, value):
        self._decision_range = value

    @property
    def symbolic(self):
        return self._symbolic

    @symbolic.setter
    def symbolic(self, value):
        self._symbolic = value

    @property
    def consistent(self):
        return self._consistent

    @consistent.setter
    def consistent(self, value):
        self._consistent = value

    def display(self):
        """Prints the dataset"""
        for attribute in self.attributes:
            sys.stdout.write(attribute + '\t')
        sys.stdout.write(self.decision + '\n')
        for case in self.universe:
            for attribute in self.attributes:
                sys.stdout.write(case.attribute_values[attribute] + '\t')
            sys.stdout.write(case.decision + '\n')

    def is_consistent(self):
        """Returns true if the dataset is consistent"""
        for case in self.universe:
            for other in self.universe:
                if case.attribute_values == other.attribute_values:
                    if case.decision != other.decision:
                        return False
        return True

    def discretize(self):
        new_attributes = []
        for attribute in self.attributes:
            if attribute_is_discretizable(attribute, self):
                attribute_values = get_sorted_numerical_attribute_values(attribute, self)
                cutpoints = get_cutpoints(attribute_values)
                min_val = min(attribute_values)
                if int(min_val) == min_val:
                    min_val = int(min_val)
                max_val = max(attribute_values)
                if int(max_val) == max_val:
                    max_val = int(max_val)
                for cutpoint in cutpoints:
                    new_attr_name = new_attribute_name(attribute, cutpoint)
                    new_attributes.append(new_attr_name)
                    option1 = str(min_val) + ".." + str(cutpoint)
                    option2 = str(cutpoint) + ".." + str(max_val)
                    self.attribute_value_ranges[new_attr_name] = [option1, option2]
                    populate_discretized_attribute(self, attribute, new_attr_name, cutpoint, min_val, max_val)
            else:
                new_attributes.append(attribute)
        self._attributes = new_attributes

class Case(object):
    def __init__(self):
        self._attribute_values = {}
        self._decision = None

    @property
    def attribute_values(self):
        return self._attribute_values

    @attribute_values.setter
    def attribute_values(self, value):
        self._attribute_values = value

    @property
    def decision(self):
        return self._decision

    @decision.setter
    def decision(self, value):
        self._decision = value
