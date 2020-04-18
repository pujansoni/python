
class ShippingContainer:
    next_serial = 1337

    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._get_next_serial

# By calling the static methods through class we prevent them from being overridden
# If we need polymorphic application then call and assign the variable through the self method