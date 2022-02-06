clean:
	find . -type d -name __pycache__ -exec rm -r {} \+

zip-src:
	find . -type d -name __pycache__ -exec rm -r {} \+
	rm -f ./dist/ig-follow-src.zip
	mkdir -p build/src
	cp -r $(shell ls -d ./src/* | grep -v test | grep -v __pycache__) build/src/
	cp handler.py __init__.py export_config.py build/
	cp .env.prod build/.env
	zip -r ./dist/ig-follow-src.zip build
	rm -rf build

.PHONY: clean zip-src
