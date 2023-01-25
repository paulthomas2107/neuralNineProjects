run:
	python mypackage/main.py

install: requirements.txt
	pip install -r requirements.txt

build: setup.py
	python setup.py build bdist_wheel

clean:
	-rm -r build
	-rm -r dist
	-rm -rf myprojectname.egg-info

