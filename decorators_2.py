import functools
# The functools.wrap() properly update metadata on wrapped functions
def noop(f):
    @functools.wraps(f)
    def noop_wrapper():
        return f()
    return noop_wrapper

@noop
def hello()
    "Print a well-known message."
    print("Hello, world!")