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

test:
    @if [ "$(shell sudo docker ps -a | grep 'mysql-test' 2> /dev/null; echo $?)" != "" ]; then\
		echo "Remove Container"; \
		sudo docker rm -f mysql-test ;\
	fi
	sudo docker run -d --name mysql-test --net host -e MYSQL_ROOT_PASSWORD=root  mysql
	python manage.py test api.tests.unit

run:
	python manage.py runserver --settings=api.config.development
 
	
default: setup
