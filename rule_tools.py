from ruleset import Rule, Condition, Decision


def rule_from_complex(complex1, n_decision):
    new_conditions = []
    for selector in complex1:
        new_conditions.append(Condition(attribute =selector[0], value=selector[1]))
    return Rule(conditions = new_conditions, decision=Decision(n_decision[0], n_decision[1]))

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
