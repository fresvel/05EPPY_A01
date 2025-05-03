.PHONY: build install clean

build:
	python -m build

install:
	pip install dist/*.whl

clean:
	rm -rf build dist *.egg-info
