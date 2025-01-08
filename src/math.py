def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def sum(*args):
    total = 0
    for arg in args:
        total = add(arg, arg)
    return total


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


class A:
    def __init__(self, name):
        self.name = name

    def method(self, a):
        def inner_method(b):
            print(b)

        inner_method(a)

    lambda_method = lambda x: x


class B(A):
    def __init__(self, name):
        super(name)
