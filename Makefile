help:
	@echo "    setup"
	@echo "        Configure the ENV using default env: APP_ENV=development."
	@echo "    tests"
	@echo "        Execute tests in application. NOTE: use make setup APP_ENV=test to install all dependencie of test"
	@echo "    setup APP_ENV={ENV}"
	@echo "        Configure using the ENV."
	@echo "    clean"
	@echo "        Clean the cache files."
	@echo "    help"
	@echo "        Show all commands."

setup: clean

	@if [ "${APP_ENV}" = "" ]; then\
		pip install -r requirements/development.txt;\
	else \
		pip install -r requirements/$(APP_ENV).txt;\
	fi

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

	rm -rf builds/

.PHONY: clean

tests: clean
	APP_ENV=test pytest --spec --cov-report term-missing --cov=notification tests/

default: setup