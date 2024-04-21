"""
collections.namedtuple() is actually a factory method that returns a subclass of the standard Python tuple type.
You feed it a type name, and the fields it should have, and it returns a class that you can instantiate,
passing in values for the fields you’ve defined, and so on.
"""

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)
print(len(sub))

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total
