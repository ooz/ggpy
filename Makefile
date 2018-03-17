all:
	pipenv run python gg.py ./

fire: all
	git commit -am "Lazy auto update `date`" | true
	git push

realfire: all
	git commit -am "Emergency update `date`" | true
	git push -f origin master

newpost:
	bash newpost.sh

# Uhhh, manual effort needed every year! Fix!
openlatest:
	@vim 2018/`ls 2018/ -t | head -n 1`

update:
	wget -q https://raw.githubusercontent.com/ooz/ggpy/master/gg.py -O gg.py
	wget -q https://raw.githubusercontent.com/ooz/ggpy/master/newpost.sh -O newpost.sh
	wget -q https://raw.githubusercontent.com/ooz/ggpy/master/Makefile -O Makefile

# Setup / dependencies
install_pipenv:
	pip3 install pipenv

install_dependencies:
	pipenv install markdown
	pipenv install pymdown-extensions

init: install_pipenv
	pipenv --three
	make install_dependencies

test: all
	pipenv install --dev pytest
	pipenv run pytest
	rm -f index.html # Side effect from testing

# Cleanup
clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '.pytest_cache' -exec rm -rf {} +
	rm -rf .cache

clean_vscode:
	rm -rf .vscode

clean_pypi:
	rm -rf dist
	rm -f *.egg-info

clean_all: clean clean_vscode clean_pypi

.PHONY: clean clean_vscode clean_pypi clean_all \
install_pipenv install_dependencies init test \
all fire realfire newpost openlatest update
