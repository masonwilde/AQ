import sys
import re
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

    def read_improved(self):
        self._file = open(self._filename, 'r')
        inpt = re.findall('\S+|\n', self._file.read())
        #rint inpt
        dataset = Dataset()
        new_case = Case()
        case_attr_index = 0
        read_mode = "normal"
        prev_mode = "normal"
        for word in inpt:
            # print "read", word
            if word[0] == "!":
                prev_mode = read_mode
                read_mode = "comment"
            elif read_mode == "comment":
                if word == "\n":
                    read_mode = prev_mode
            elif read_mode == "ignore":
                if word == ">":
                    # print "Ending ignore"
                    read_mode = prev_mode
            elif word != "\n":
                if read_mode == "normal":
                    if word == "<":
                        # print "start ignore"
                        prev_mode = read_mode
                        read_mode = "ignore"
                    if word == "[":
                        # print "start labels"
                        prev_mode = read_mode
                        read_mode = "labels"
                elif read_mode == "labels":
                    if word == "]":
                        # print "make dataset decision be", dataset.attributes[-1]
                        dataset.decision = dataset.attributes[-1]
                        del dataset.attributes[-1]
                        read_mode = "cases"
                    else:
                        # print "adding dataset attribute", word
                        dataset.attributes.append(word)
                        if word not in dataset.attribute_value_ranges:
                            dataset.attribute_value_ranges[word] = []
                elif read_mode == "cases":
                    if case_attr_index == len(dataset.attributes):
                        new_case.decision = word
                        if word not in dataset.decision_range:
                            dataset.decision_range.append(word)
                        dataset.universe.append(new_case)
                        new_case = Case()
                        case_attr_index = 0
                    else:
                        new_case.attribute_values[dataset.attributes[case_attr_index]] = word
                        if word not in dataset.attribute_value_ranges[dataset.attributes[case_attr_index]]:
                            dataset.attribute_value_ranges[dataset.attributes[case_attr_index]].append(word)
                        case_attr_index += 1
        return dataset
