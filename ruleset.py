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

    def to_string(self):
        rule = ""
        for i, condition in enumerate(self.conditions):
            if i > 0:
                rule += "& "
            rule += "(" + condition.attribute + ", not " + condition.value + ") "
        rule += "-> (" + self.decision.label + ", " + self.decision.value + ")"
        return rule

class Ruleset(object):
    def __init__(self):
        self._rules = []

    @property
    def rules(self):
        return self._rules

    @rules.setter
    def rules(self, value):
        self._rules = value

    def display(self):
        for rule in self.rules:
            print rule.to_string()

    def print_to_file(self, filename, negated=True):
        f = open(filename, 'w')
        for rule in self.rules:
            f.write(rule.to_string() + '\n')
        f.closed
