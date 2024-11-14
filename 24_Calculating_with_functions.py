"""This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))"""


def zero(*args):
    if args:
        return args(0)
    return 0


def one():
    pass  # your code here


def two():
    pass  # your code here


def three():
    pass  # your code here


def four():
    pass  # your code here


def five():
    pass  # your code here


def six():
    pass  # your code here


def seven(fn=None):
    return 7 if fn is None else fn(7)


def eight():
    pass  # your code here


def nine(fn=None):
    return 9 if fn is None else fn(9)


def plus(b):
    return lambda a: a + b


def minus():
    pass  # your code here


def times():
    pass  # your code here


def divided_by():
    pass  # your code here


print(nine(plus(nine())))
