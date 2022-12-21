.PHONY: test

install:
	pip install .

test:
	pip install .
	pytest

repl: install
	sgl