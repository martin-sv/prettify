from behave import *
import math

@given('we choose "{number}" as an input number')
def impl(context, number):
    number_tfloat = float(number)
    
    if (math.floor(number_tfloat) == number_tfloat):
        context.number = int(number_tfloat)
    else:
        context.number = number_tfloat
        
@when('we simplify it')
def impl(context):
    context.stored_answer = simplify(context.number)

@then('we should get the "{answer}" as result')
def impl(context, answer):
    assert context.stored_answer == answer