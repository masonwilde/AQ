import sys

def attribute_is_discretizable(attribute, dataset):
    try:
        x = float(dataset.universe[0].attribute_values[attribute])
        return True
    except:
        return False

def get_sorted_numerical_attribute_values(attribute, dataset):
    vals = []
    for case in dataset.universe:
        numerical_val = 0
        try:
            numerical_val = int(case.attribute_values[attribute])
        except:
            numerical_val = float(case.attribute_values[attribute])
        if numerical_val not in vals:
            vals.append(numerical_val)
    return sorted(vals)

class Dataset(object):

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
        for attribute in self.attributes:
            sys.stdout.write(attribute + '\t')
        sys.stdout.write(self.decision + '\n')
        for case in self.universe:
            for attribute in self.attributes:
                sys.stdout.write(case.attribute_values[attribute] + '\t')
            sys.stdout.write(case.decision + '\n')

    def is_consistent(self):
        for case in self.universe:
            for other in self.universe:
                if case.attribute_values == other.attribute_values:
                    if case.decision != other.decision:
                        return False
        return True

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
