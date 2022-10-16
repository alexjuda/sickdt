.PHONY: test build publish-test-pypi clean

test:
	pytest tests

build:
	python -m build

publish-test-pypi:
	twine upload -r testpypi dist/*

clean:
	rm -r build dist
