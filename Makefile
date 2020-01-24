.PHONY: run
run :
	python2 time_connectivity.py

.PHONY: format
format :
	black time_connectivity.py
