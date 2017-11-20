# Name: Mason Wilde
# KUID: 2645990
# Course: EECS 690
# Professor: Dr Jerzy Gryzmala-Busse
# Semester: Fall 2017
# Project: AQ Rule Inducer
# File: aq_tools.py
# Date Modified:  2017-11-19
"""Suite of tools used in the AQ method of rule induction"""
from ruleset import Ruleset
import rule_tools

def combine_complex(complex1, complex2):
    """Combines two complexes into one result containing the selectors from each input"""
    new_complex = []
    for selector1 in complex1:
        new_complex.append(selector1)
    for selector2 in complex2:
        if selector2 not in new_complex:
            new_complex.append(selector2)
    return new_complex

def disjunction(star1, star2, maxstar):
    """Returns the disjunction of two stars, not allowing it to exceed a size of maxstar"""
    new_star = []
    for complex1 in star1:
        for complex2 in star2:
            new_star.append(combine_complex(complex1, complex2))
            if len(new_star) >= maxstar:
                return new_star
    return new_star

def cases_covered_by_complex(dataset, complex1):
    """Returns a list of case numbers covered by a complex"""
    cases = []
    for i, case in enumerate(dataset.universe):
        if case_covered_by_complex(case, complex1):
            cases.append(i)
    return cases

def case_covered_by_complex(case, complex1):
    """Returns true if a case is covered by the complex, false otherwise"""
    for selector in complex1:
        if case.attribute_values[selector[0]] == selector[1]:
            return False
    return True

def cases_covered_by_star(dataset, star):
    """Returns a list of case numbers covered by a star"""
    cases = []
    for complex1 in star:
        cases = list(set(cases) | set(cases_covered_by_complex(dataset, complex1)))
    return cases

def make_star(attributes, case1, case2):
    """Return a partial star for the difference between two cases"""
    star = []
    for attribute in attributes:
        if case1.attribute_values[attribute] != case2.attribute_values[attribute]:
            star.append([[attribute, case2.attribute_values[attribute]]])
    return star

def get_cases_in_concept(dataset, decision_value):
    """Returns a list of case numbers in a given concept"""
    cases =[]
    for i, case in enumerate(dataset.universe):
        if case.decision == decision_value:
            cases.append(i)
    return cases

def get_concepts(dataset):
    """Returns a list of concepts (list of case numbers) in a dataset"""
    concepts = []
    for cur_decision in dataset.decision_range:
        cases = get_cases_in_concept(dataset, cur_decision)
        new_concept = [[dataset.decision, cur_decision], cases]
        concepts.append(new_concept)
    return concepts

def complex_is_superset(complex1, complex2):
    """Returns true if a complex is a superset of another"""
    for selector in complex2:
        if selector not in complex1:
            return False
    for selector in complex1:
        if selector not in complex2:
            return True
    return False

def make_star_for_concept(dataset, concept, maxstar):
    """Returns a list of completed stars for a given concept"""
    stars = []
    concept_cases = concept[1]
    all_cases = range(len(dataset.universe))
    F = list(set(all_cases) - set(concept_cases))
    cases_to_cover = concept_cases
    while cases_to_cover:
        star = [[]]
        # This loop can be optimized by only looking at non-concept cases_covered
        # that are still covered, but this becomse inefficient after maxstar of about 70
        for bad_case in F:
            partial_star = make_star(dataset.attributes, dataset.universe[cases_to_cover[0]], dataset.universe[bad_case])
            star = disjunction(star, partial_star, maxstar)
        # remove superset complexes
        if len(star) > 1:
            trimmed_star = []
            for i in range(len(star)):
                i_is_superset = False
                for j in range(len(star)):
                    if i != j:
                        if complex_is_superset(star[i], star[j]):
                            i_is_superset = True
                if not i_is_superset:
                    trimmed_star.append(star[i])
                    #print "adding ", star[i]
            star = trimmed_star
        # # Keep only the star that covers the most cases
        star = [max(star, key=lambda c: len(cases_covered_by_complex(dataset, c)))]
        #star = [star[0]]
        stars.append(star)
        covered_cases = []
        for star in stars:
            covered_cases = list(set(covered_cases).union(set(cases_covered_by_star(dataset, star))))
        cases_to_cover = list(set(concept_cases) - set(covered_cases))
    return stars

def induce(dataset, maxstar, file_title, checks=False):
    """Induce rules with and withour negation for a LERS format ruleset"""
    concept_stars = []
    ruleset = Ruleset()
    unnegated_ruleset = Ruleset()
    for concept in get_concepts(dataset):
        #print "Working on concept ", concept
        concept_stars.append([concept[0], make_star_for_concept(dataset, concept, maxstar)])
    for concept in concept_stars:
        decision = concept[0]
        stars = concept[1]
        for star in stars:
            for complex1 in star:
                ruleset.rules.append(rule_tools.rule_from_complex(complex1, decision))
    unnegated_ruleset.rules = ruleset.unnegate(dataset)
    # print "Rules with Negation"
    # self._ruleset.display()
    ruleset.print_to_file(filename=file_title+".with.negation.rul")

    # print "Rules without Negation"
    # self._unnegated_ruleset.display(negated=False)
    unnegated_ruleset.print_to_file(filename=file_title+".without.negation.rul", negated=False)

    if checks:
        print "Negated ruleset is consistent:", ruleset.is_consistent(dataset)
        print "Negated ruleset is complete:", ruleset.is_complete(dataset)
        print "Unnegated ruleset is consistent:", unnegated_ruleset.is_consistent(dataset, negated=False)
        print "Unnegated ruleset is complete:", unnegated_ruleset.is_complete(dataset, negated=False)
