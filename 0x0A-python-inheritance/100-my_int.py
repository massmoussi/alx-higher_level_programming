#!/usr/bin/python3


"""Class MyInt Inherent from built-in Class"""


class MyInt(int):
    """
    use the __eq__ to check the equality
    use the __ne__ to check the inequality
    Since we want invert result we use not Operator
    """
    def __eq__(self, other):
        return not super().__eq__(other)

    def __ne__(self, other):
        return not super().__ne__(other)
