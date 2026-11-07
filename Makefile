PYTHON ?= python3

.PHONY: run test

run:
	$(PYTHON) financial_calculator.py

test:
	$(PYTHON) -m pytest test_financial_calculator.py
