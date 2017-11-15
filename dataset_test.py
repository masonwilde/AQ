import unittest
import dataset
from lers_reader import Lers_Reader

reader = Lers_Reader("numerical_consistent.d")
mock_dataset = reader.read()


class TestDataset(unittest.TestCase):
    def test_attribute_is_discretizable_true(self):
        self.assertTrue(dataset.attribute_is_discretizable('Temperature', mock_dataset))
    def test_attribute_is_discretizable_false(self):
        self.assertFalse(dataset.attribute_is_discretizable('Headache', mock_dataset))

if __name__ == '__main__':
    unittest.main()
