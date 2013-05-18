from behave import *
import math

@given('we choose "{number}" as an input number')
def impl(context, number):
    context.number = float(number) if '.' in number else int(number)
        
@when('we simplify it')
def impl(context):
    context.stored_answer = simplify(context.number)

@then('we should get the "{answer}" as result')
def impl(context, answer):
    assert context.stored_answer == answer
