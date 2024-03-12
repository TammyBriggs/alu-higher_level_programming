#!/usr/bin/python3
"""Making a class"""
class Square:
    """Class Square which has a private instance"""

    def __init__(self, size=0):
        """init size"""
        self.__size = size

    @property
    def size(self):
        """Returning the attribute of size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Asigning size to the size attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Defining size area"""
        square_area = self.__size ** 2
        return square_area
    
    def my_print(self):
        """prints squared num from above starting with # before number e.g #9"""
        if self.__size == 0:
            print()
        else: 
            for i in range(self.__size):
                for n in range(self.__size):
                    print("#", end="")
                print()
