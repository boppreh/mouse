test: tests

tests:
	coverage2 run -am mouse._mouse_tests
	coverage3 run -am mouse._mouse_tests && coverage3 report && coverage3 html

release:
	python make_release.py

readme:
	python ../docstring2markdown/docstring2markdown.py mouse "https://github.com/boppreh/mouse/blob/master" > README.md

clean:
	rm -rfv dist build coverage_html_report mouse.egg-info

install:
	pip install .

all: clean tests readme release
