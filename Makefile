build:
	rm -rf build
	mkdir build
	zip build/main.zip main.py index.html

.PHONY: build
