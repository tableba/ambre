PYTHON ?= python # python3 py

all:start

coverage:
	coverage run -m unittest discover
	coverage html

docs:
	pdoc --html --output-dir docs/pdoc *.py

venv:
	$(PYTHON) -m venv .venv
	@printf "Now you have to activate the virual environement.\n"
	@printf "[On Mac/Linux] -- . .venv/bin/activate\n"
	@printf "[On Windows] -- . .venv/Scripts/activate\n"
	@printf "Type 'deactivate' to deactivate"

start:
	$(PYTHON) src/main.py


clean-docs:
	rm -rf html
	rm -rf docs


clean:
	rm -rf htmlcov
	rm -rf __pycache__


