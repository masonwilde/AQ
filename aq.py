from ruleset import Ruleset
from dataset import Dataset
import aq_tools
import rule_tools

def make_star_for_concept(dataset, concept, maxstar):
    #print concept
    stars = []
    concept_cases = concept[1]
    all_cases = range(len(dataset.universe))
    F = list(set(all_cases) - set(concept_cases))
    cases_to_cover = concept_cases
    while cases_to_cover:
        #print "Cases to cover", cases_to_cover
        star = [[]]
        for bad_case in F:
            partial_star = aq_tools.make_star(dataset.attributes, dataset.universe[cases_to_cover[0]], dataset.universe[bad_case])
            star = aq_tools.disjunction(star, partial_star, maxstar)
        stars.append(star)
        covered_cases = []
        for star in stars:
            covered_cases = list(set(covered_cases).union(set(aq_tools.cases_covered_by_star(dataset, star))))
        cases_to_cover = list(set(concept_cases) - set(covered_cases))
    #print stars
    return stars


class AQ(object):
    def __init__(self, maxstar, dataset = Dataset()):
        self._dataset = dataset
        self._ruleset = Ruleset()
        self._maxstar = maxstar

    def induce(self):
        concept_stars = []
        for concept in aq_tools.get_concepts(self._dataset):
            concept_stars.append([concept[0], make_star_for_concept(self._dataset, concept, self._maxstar)])
        for concept in concept_stars:
            decision = concept[0]
            stars = concept[1]
            for star in stars:
                for complex1 in star:
                    self._ruleset.rules.append(rule_tools.rule_from_complex(complex1, decision))
        self._ruleset.display()
