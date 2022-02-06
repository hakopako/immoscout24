download-lib:
	pip3 install -r requirements.txt -t ./src/

clean:
	find . -type d -name __pycache__ -exec rm -r {} \+

zip-src:
	find . -type d -name __pycache__ -exec rm -r {} \+
	rm -f ./dist/immoscout24.zip
	cd src && zip -r immoscout24.zip urllib3 *.py -x test_* && mv -f immoscout24.zip ../dist/

.PHONY: clean zip-src
