# This example is same as the class_attributes.py file, but this example use the @staticmethod decorator to have the same effect
class ShippingContainer:
    next_serial = 1337

    @staticmethod
    def _get_next_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = self._get_next_serial