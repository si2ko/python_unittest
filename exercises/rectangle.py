import unittest

def rectangle(width, height):
    """Function that calculate area of rectanlge"""

    if not (isinstance(width,(int,float)) and isinstance(height,(int, float))):
        raise TypeError('Instances must be int or float type')

    if not (height > 0 and width > 0):
        raise ValueError('Instances must be above zero')

    return width * height


def perimeter(width, height):
    """Function that calculate area of rectanlge"""

    if not (isinstance(width,(int,float)) and isinstance(height,(int, float))):
        raise TypeError('Instances must be int or float type')

    if not (height > 0 and width > 0):
        raise ValueError('Instances must be above zero')

    return 2 * width + 2 * height

