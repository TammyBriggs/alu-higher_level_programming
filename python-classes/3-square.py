#!/usr/bin/python3
"""creating class"""
class Square:
    """Private instance is size"""
    def __init__(self, size=0):
        """controlled if statements below"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """defining shape area"""
        square_area = self.__size ** 2
        return square_area
