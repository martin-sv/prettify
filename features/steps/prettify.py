#!/usr/bin/env python
postfix_letters = ['', '', 'M', 'B', 'T', 'x10^15']
minium_order = 6

def number_order(number):
    order = (len(str(int(number))) - 1)
    return order


def postfix(order):
    pow_thousand = int(order / 3)

    if pow_thousand >= (len(postfix_letters)):
        raise Exception("size not supported")
    else:
        return postfix_letters[pow_thousand]


def split_number(number, digits):
    separator = len(str(int(number))) - int(digits / 3) * 3
    return [str(number)[:separator], str(number)[separator:]]


def truncate(number, order):
    integer_part, rest_number = split_number(number, order)

    if float(rest_number) != 0:
        return (int(integer_part) + float("0." + str(rest_number)[0]))
    else:
        return integer_part


def simplify(number):
    order = number_order(number)

    if order < minium_order:
        return str(number)
    else:
        result = str(truncate(number, order)) + postfix(order)
        return result
