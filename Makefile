run:
	python main.py

test:
	python aq_tools_test.py
	python rule_tools_test.py
	python ruleset_test.py
	python dataset_test.py

clean:
	rm *.pyc
	rm *.rul
