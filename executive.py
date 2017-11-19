# Name: Mason Wilde
# KUID: 2645990
# Course: EECS 690
# Professor: Dr Jerzy Gryzmala-Busse
# Semester: Fall 2017
# Project: AQ Rule Inducer
# File: executive.py
# Date Modified:  2017-11-19

from lers_reader import Lers_Reader
import aq_tools

def run(checks=False):

    # Get and open file from the user
    file_open = False
    while not file_open:
        filename = raw_input("Please enter a filename: ")
        try:
            file_test = open(filename, 'r')
            file_open = True
        except IOError:
            print "File could not be opened"
            file_open = False
    # End file name retrieval

    # Get maxstar value from the user
    maxstar_obtained = False
    maxstar = None
    while not maxstar_obtained:
        maxstar = raw_input("Please enter an integer value for MAXSTAR: ")
        try:
            maxstar = int(maxstar)
            if maxstar > 0:
                maxstar_obtained = True
            else:
                print "Invalid Maxstar value. Please enter an integer larger than 0."
        except ValueError:
            print "Invalid Maxstar value. Please enter an integer larger than 0."
    # End maxstar retrieval
    #get path without extension
    file_title = ('.').join(filename.rsplit('.')[:-1])
    reader = Lers_Reader(filename)
    # print "File opened"
    # dataset = reader.read()
    # dataset.display()
    dataset = reader.read_improved()
    #dataset.display()
    # print "Dataset read"
    # print "Beginning Discretization Process"
    dataset.discretize()
    # print "Discretization Complete"
    #dataset.display()
    #dataset.discretize()
    if not dataset.is_consistent():
        with open("my-data.with.negation.rul", 'w') as f:
            f.write("! The input data set is inconsistent\n")
        with open("my-data.without.negation.rul", 'w') as f:
            f.write("! The input data set is inconsistent\n")
        print "Dataset is inconsistent"
        print "No rules induced"
        return
    else:
        aq_tools.induce(dataset, maxstar, file_title, checks)
        print "Done."
