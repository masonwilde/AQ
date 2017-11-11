def combine_complex(complex1, complex2):
    new_complex = []
    for selector1 in complex1:
        new_complex.append(selector1)
    for selector2 in complex2:
        if selector2 not in new_complex:
            new_complex.append(selector2)
    return new_complex

def disjunction(star1, star2, maxstar):
    new_star = []
    for complex1 in star1:
        for complex2 in star2:
            new_star.append(combine_complex(complex1, complex2))
            if len(new_star) >= maxstar:
                return new_star
    return new_star

def cases_covered_by_complex(dataset, complex1):
    cases = []
    for i, case in enumerate(dataset.universe):
        if case_covered_by_complex(case, complex1):
            cases.append(i)
    return cases

def case_covered_by_complex(case, complex1):
    for selector in complex1:
        if case.attribute_values[selector[0]] == selector[1]:
            return False
    return True

def cases_covered_by_star(dataset, star):
    cases = []
    for complex1 in star:
        cases = list(set(cases) | set(cases_covered_by_complex(dataset, complex1)))
    return cases

def make_star(attributes, case1, case2):
    star = []
    for attribute in attributes:
        if case1.attribute_values[attribute] != case2.attribute_values[attribute]:
            star.append([[attribute, case2.attribute_values[attribute]]])
    return star

def get_cases_in_concept(dataset, decision_value):
    cases =[]
    for i, case in enumerate(dataset.universe):
        if case.decision == decision_value:
            cases.append(i)
    return cases

def get_concepts(dataset):
    concepts = []
    for cur_decision in dataset.decision_range:
        cases = get_cases_in_concept(dataset, cur_decision)
        new_concept = [[dataset.decision, cur_decision], cases]
        concepts.append(new_concept)
    return concepts
