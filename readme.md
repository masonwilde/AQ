EECS 690 AQ Project

**To run:**

All methods assume a Unix based system, If you are working on a different system, simply run AQ.py using a Python2.7 interpreter

* Method 1:
  In a Unix shell Terminal
    Enter `make run` in a Linux terminal with Python 2.7 installed
* Method 2 (no make support):
  In a Unix shell Terminal
    Enter `python AQ.py`

If none of the previous methods work, ensure that your version of Python is 2.7,
  and run AQ.py using a Python 2.7 Interpreter

**To verify rules**

This process is capable of reading a dataset in LERS format, along with rules
of the form "(attribute1, not value1) & (attribute2, not value2) -> (decision, value)",
and then confirming that the ruleset is complete and consistent

* Method 1:
  In a Unix Shel terminal
    Enter `make verify data="path/to/dataset.txt" rules="path/to/rules.rul" negation="with|without"`

* Method 2:
  In a Unix Shel terminal
    Enter `python verify_rules.py "path/to/dataset.txt" "path/to/rules.rul" [with|without]`
