# Name: Mason Wilde
# KUID: 2645990
# Course: EECS 690
# Professor: Dr Jerzy Gryzmala-Busse
# Semester: Fall 2017
# Project: AQ Rule Inducer
# File: Makefile
# Date Modified: 2017-11-19

run:
	python AQ.py

verify:
	python verify_rules.py ${data} ${rules} ${negation}

test:
	python aq_tools_test.py
	python rule_tools_test.py
	python ruleset_test.py
	python dataset_test.py

clean:
	rm *.pyc
	rm *.rul
