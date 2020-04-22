class Base:
    def __init__(self):
        print('Base initializer')

    def f(self):
        print('Base.f()')

class Sub(Base):
    def __init__(self):
        super().__init__()
        print('Sub initializer')

    def f(self):
        print('Sub.f()')

# The empty Sub class can be declared as:
# class Sub(Base):
#     pass

# Other languages automatically call base class initializers
# Python treats __init__() like any other method
# Base class __init__() is not called if overridden
# Use super() to call base class __init__()