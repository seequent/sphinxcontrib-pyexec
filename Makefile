
.PHONY: install publish test coverage lint graph docs

install:
	python setup.py install

publish:
	python setup.py sdist upload

test:
	nosetests

docs:
	cd docs && make html

coverage:
	nosetests --logging-level=INFO --with-coverage --cover-package=pyexec --cover-html
	open cover/index.html

lint:
	pylint --output-format=html pyexec > pylint.html

graphs:
	pyreverse -my -A -o pdf -p pyexec pyexec/**.py pyexec/**/**.py
