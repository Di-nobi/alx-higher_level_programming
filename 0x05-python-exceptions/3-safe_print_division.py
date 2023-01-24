#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
    except ZeroDivisionError:
        div = 0
    except TypeError:
        div = 0
    finally:
        print("Inside result: {}".format(div))
    return (div)
