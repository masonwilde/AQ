import sys
from dataset import Dataset, Case

class Lers_Reader(object):

    def __init__(self, filename):
        self._filename = filename

    def read(self):
        self._file = open(self._filename, 'r')
        dataset = Dataset()
        for row_of_data in self._file:
            head, separator, tail = row_of_data.partition('!')
            row_of_data = head.strip()
            if row_of_data == "" or row_of_data[0] == '<' or row_of_data.isspace():
                continue
            elif row_of_data[0] == '[':
                split_row_of_data = row_of_data.split()
                del split_row_of_data[0]
                del split_row_of_data[-1]
                dataset.decision = split_row_of_data[-1]
                del split_row_of_data[-1]
                for attribute in split_row_of_data:
                    dataset.attributes.append(attribute)
                    dataset.attribute_value_ranges[attribute] = []
            else:
                split_row_of_data = row_of_data.split()
                case = Case()
                case.decision = split_row_of_data[-1]
                if case.decision not in dataset.decision_range:
                    dataset.decision_range.append(case.decision)
                del split_row_of_data[-1]
                for i, value in enumerate(split_row_of_data):
                    case.attribute_values[dataset.attributes[i]] = value
                    if value not in dataset.attribute_value_ranges[dataset.attributes[i]]:
                        dataset.attribute_value_ranges[dataset.attributes[i]].append(value)
                dataset.universe.append(case)
        return dataset
