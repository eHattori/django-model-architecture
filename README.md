# Django Model Architecture

This is a Model of API REST using Django Framework

## Getting Started

### Dependencies

* Python 3.5.3
* MySQL

The project is prepared for work with:

* Django 1.11
* Burzum Log
* Swagger
* Circle CI
* Teresa

### Installation

1. Clone the repository in your machine.
2. Run `mkvirtualenv django-model-architecture` to create a new virtualenv.
3. Switch between env with `workon django-model-architecture`.
4. Run `make setup ` to install.
5. Run the script sql in your database `CREATE DATABASE api_django;`
6. Run `make migrate`

# Documentation

Execute the app with `make run` and access the documentation of API with swagger

`https://localhost:8000/`

# Tests

Run `make test`

# LICENSE

Code released under the MIT License.

#BackLog:

BDD - (working with behave ...)
OAuth2
APIGee return pattern

