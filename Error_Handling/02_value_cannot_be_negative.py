class ValueCannotBeNegative(Exception):
    """ Raised if a given number is negative """
    pass


for _ in range(5):
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegative
