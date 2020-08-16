name = "Eric"
age = 74
print(f"Hello, {name}. You are {age}.")
print(F"Hello, {name}. You are {age}.")
print(f"{2 * 37}")

# But you could also call functions. Here’s an example:


def to_lowercase(input):
    return input.lower()

name = "Eric Idle"
print(f"{to_lowercase(name)} is funny")

# You also have the option of calling a method directly:
print(f"{name.lower()} is funny")

# You could even use objects created from classes with f-strings. Imagine you had the following class:
class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"

# You’d be able to do this:
new_comedian = Comedian("Eric", "Idle", "74")
print(f"{new_comedian}")

# The __str__() and __repr__() methods deal with how objects are presented as strings,
# so you’ll need to make sure you include at least one of those methods in your class definition.
# If you have to pick one, go with __repr__() because it can be used in place of __str__().
# The string returned by __str__() is the informal string representation of an object and should be readable.
# The string returned by __repr__() is the official representation and should be unambiguous.
# Calling str() and repr() is preferable to using __str__() and __repr__() directly.
# By default, f-strings will use __str__(), but you can make sure they use __repr__() if you include the conversion flag !r:
print(f"{new_comedian}")
print(f"{new_comedian!r}")

# Multiline f-strings
name = "Eric"
profession = "comedian"
affiliation = "Monty Python"
message = (
    f"Hi {name}. "
    f"You are a {profession}. "
    f"You were in {affiliation}."
)
print(message)
# But remember that you need to place an f in front of each line of a multiline string. The following code won’t work:
message = (
    f"Hi {name}. "
    "You are a {profession}. "
    "You were in {affiliation}."
)
print(message)

# If you want to spread strings over multiple lines, you also have the option of escaping a return with a \:
message = f"Hi {name}. " \
    f"You are a {profession}. " \
    f"You were in {affiliation}."
print(message)