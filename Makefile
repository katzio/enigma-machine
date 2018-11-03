init:
	pip install -r requirements.txt

install:
	pip install . --update

test:
	nosetests -v tests/test_enc.py
	nosetests -v tests/test_dec.py
	python tests/performance_test.py
