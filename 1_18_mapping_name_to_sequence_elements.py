from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('abc@gmail.com', '2010-02-02')
print(sub)
print(sub.addr)
print(sub.joined)

# Reference to positional elements often make the code a bit less expensive and more
# dependent on the structure of the records. Here is a version that uses a namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

# If you need to change any of the attributes, it can be done using the _replace() method
# of a namedtuple instance, which makes an entirely new namedtuple with specified values
# replaced
s = Stock1('ACME', 100, 123.45)
s = s._replace(shares=75)
print(s)

# A subtle use of the _replace() method is that it can be a convenient way to populate
# named tuples that have optional or missing field. To do this, you make a prototype
# tuple containing the default values and then use _replace() to create new instances 
# with values replaced.
Stock2 = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)
# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))