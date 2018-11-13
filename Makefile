install:
	pip install -r requirements_dev.txt

test:
	python -m pytest -v -rfs -s --disable-pytest-warnings enigma/tests/test_enc.py

p-test:
	python enigma/tests/performance_test.py
