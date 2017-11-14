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
