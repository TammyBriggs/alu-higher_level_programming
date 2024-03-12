#!/usr/bin/python3
"""Some code may appear here"""
class Square:
    """Square is a class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize variables."""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """defining size"""
        return self.__size

    @size.setter
    def size(self, size):
        """if statments incase wrong input"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def __init__(self, size=0, position=(0, 0)):
        """Initialise size attribute"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns size attribute data"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size to a value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Makes square postion a value and verifies type of value"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns square area"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for n in range(self.__size):
                for x in range(self.__position[0]):
                    print(' ', end="")
                for q in range(self.__size):
                    print("#", end="")
                print()
