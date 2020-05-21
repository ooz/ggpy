all:
	pipenv run python gg.py ./

fire: all
	git commit -am "Lazy auto update `date`" || true
	git push

realfire: all
	git commit -am "Emergency update `date`" || true
	git push -f origin master

newpost:
	bash newpost.sh

openlatest:
	@ls -1t `find . -type f -name '*.md'` | head -n 1 | xargs -o vim

update:
	wget -q https://raw.githubusercontent.com/ooz/ggpy/master/gg.py -O gg.py
	wget -q https://raw.githubusercontent.com/ooz/ggpy/master/Pipfile -O Pipfile
	wget -q https://raw.githubusercontent.com/ooz/ggpy/master/newpost.sh -O newpost.sh
	@echo "Unfortunately the Makefile cannot be updated automatically!"
	@echo "Run the following command to update:"
	@echo "wget -q https://raw.githubusercontent.com/ooz/ggpy/master/Makefile -O Makefile"

# Setup / dependencies / CI/CD
install_pipenv:
	pip3 install pipenv

init:
	pipenv --python 3
	pipenv install

test: | clean_coverage
	pipenv install --dev
	pipenv run coverage run --source=. -m pytest -vv
	pipenv run coverage html --omit="test/*"
	pipenv run coverage report --omit="test/*"

deploy: all
	git add .
	git commit -am "Build by CircleCI `date` [skip ci]" || true
	git push

# Cleanup
clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '.pytest_cache' -exec rm -rf {} +
	rm -rf .cache
	rm -rf dist
	rm -f *.egg-info
	pipenv --rm || true

clean_coverage:
	rm -rf htmlcov/
	rm -f .coverage

.PHONY: clean clean_coverage \
install_pipenv init test deploy \
all fire realfire newpost openlatest update
