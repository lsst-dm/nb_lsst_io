.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of:"
	@echo "  init       to initialize a dev environment"
	@echo "  clean      clear tox environments and builds"

.PHONY: init
init:
	pip install tox
	rm -rf tox

.PHONY: clean
clean:
	rm -rf _build/*
	rm -rf .tox
