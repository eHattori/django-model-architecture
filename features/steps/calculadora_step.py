from behave import *
from api.services.calculadora_service import Calculadora
from hamcrest import *

@given('Dado que eu tenho uma calculadora')
def step_impl(context):
    context.calculadora = Calculadora(1,2)
    pass


@when('Quando eu entro com 1 e 2')
def step_impl(context):
    assert True is not False

@when('quando a somatória é feita')
def step_impl(context):
    context.resultado = context.calculadora .soma()
    assert True is not False

@then('Então o resultado dever ser 3')
def step_impl(context):
    assert_that(context.resultado , equal_to(3))
    assert context.failed is False