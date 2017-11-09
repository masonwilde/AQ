import unittest
import aq_tools


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

if __name__ == '__main__':
    unittest.main()
