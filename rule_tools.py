from ruleset import Rule, Condition, Decision


def rule_from_complex(complex1, n_decision):
    new_conditions = []
    for selector in complex1:
        new_conditions.append(Condition(attribute =selector[0], value=selector[1]))
    return Rule(conditions = new_conditions, decision=Decision(n_decision[0], n_decision[1]))
