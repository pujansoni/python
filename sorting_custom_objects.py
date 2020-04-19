# The built-in sorted() function takes a key argument that can be passed a callable that
# will return some value in the object that sorted will use to compare the objects. For
# example, if you have a sequence of User instances in your application, and you want to
# sort them by their user_id attribute, you would supply a callable that takes a User
# instance as input and returns the user_id
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]
print(users)
print(sorted(users, key=lambda u: u.user_id))

# Instead of using lambda, an alternative approach is to use operator.attrgetter()
from operator import attrgetter
print(sorted(users, key=attrgetter('user_id')))

# The choice of whether or not to use lambda or attrgetter() may be one of personal preference. 
# However, attrgetter() is often a tad bit faster and also has the added
# feature of allowing multiple fields to be extracted simultaneously. This is analogous to
# the use of operator.itemgetter() for dictionaries
# Ex: sorted(users, key=attrgetter('last_name', 'first_name'))