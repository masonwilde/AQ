import unittest
import aq_tools
from lers_reader import Lers_Reader

reader = Lers_Reader("simple_consistent.d")
mock_dataset = reader.read()


class TestAQTools(unittest.TestCase):
    def test_combine_complexes_simple(self):
        complex1 = [["Temp", "low"], ["Cough", "no"]]
        complex2 = [["Headache", "yes"]]
        new_complex = aq_tools.combine_complex(complex1, complex2)
        self.assertEqual(new_complex, [["Temp", "low"], ["Cough", "no"], ["Headache", "yes"]])
    def test_combine_complexes_harder(self):
        complex1 = [["Temp", "low"], ["Cough", "no"]]
        complex2 = [["Temp", "low"]]
        new_complex = aq_tools.combine_complex(complex1, complex2)
        self.assertEqual(new_complex, [["Temp", "low"], ["Cough", "no"]])
    def test_disjunction_single_complex_single_selector(self):
        star1 = [[["Temp", "low"]]]
        star2 = [[["Headache", "yes"]]]
        new_star = aq_tools.disjunction(star1, star2, 10)
        self.assertEqual(new_star, [[["Temp", "low"], ["Headache", "yes"]]])
    def test_disjunction_single_complex_multi_selector(self):
        star1 = [[["Temp", "low"], ["Cough", "no"]]]
        star2 = [[["Headache", "yes"], ["Cough", "no"]]]
        new_star = aq_tools.disjunction(star1, star2, 10)
        self.assertEqual(new_star, [[["Temp", "low"], ["Cough", "no"], ["Headache", "yes"]]])
    def test_disjunction_multi_complex_single_selector(self):
        star1 = [[["Temp", "low"]], [["Cough", "no"]]]
        star2 = [[["Headache", "yes"]], [["Cough", "no"]]]
        new_star = aq_tools.disjunction(star1, star2, 10)
        self.assertEqual(new_star, [[["Temp", "low"], ["Headache", "yes"]], [["Temp", "low"], ["Cough", "no"]],
                                    [["Cough", "no"], ["Headache", "yes"]], [["Cough", "no"]]])
    def test_disjunction_multi_complex_single_selector_limit_maxstar(self):
        star1 = [[["Temp", "low"]], [["Cough", "no"]]]
        star2 = [[["Headache", "yes"]], [["Cough", "no"]]]
        new_star = aq_tools.disjunction(star1, star2, 3)
        self.assertEqual(new_star, [[["Temp", "low"], ["Headache", "yes"]], [["Temp", "low"], ["Cough", "no"]],
                                    [["Cough", "no"], ["Headache", "yes"]]])

    def test_cases_covered_by_complex_simple(self):
        result = aq_tools.cases_covered_by_complex(mock_dataset, [["Temperature", "high"]])
        self.assertEqual(result, [1,2,5,6])

    def test_cases_covered_by_complex_advanced(self):
        result = aq_tools.cases_covered_by_complex(mock_dataset, [["Temperature", "high"], ["Headache", "yes"]])
        self.assertEqual(result, [2,6])

    def test_cases_covered_by_complex_super_advanced(self):
        result = aq_tools.cases_covered_by_complex(mock_dataset, [["Temperature", "high"], ["Headache", "yes"], ["Nausea", "no"]])
        self.assertEqual(result, [6])

if __name__ == '__main__':
    unittest.main()
