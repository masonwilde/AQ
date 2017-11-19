# Name: Mason Wilde
# KUID: 2645990
# Course: EECS 690
# Professor: Dr Jerzy Gryzmala-Busse
# Semester: Fall 2017
# Project: AQ Rule Inducer
# File: AQ.py
# Date Modified:  2017-11-19

#!/usr/bin/env python

import sys
import executive

def main():
    checks=False
    if len(sys.argv)>1:
        if sys.argv[1] == "-verify":
            checks=True
    executive.run(checks)


if __name__ == "__main__":
    main()
