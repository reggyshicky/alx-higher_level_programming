#!/usr/bin/python3
"""
module documentation
"""


class Square():
    """A class that defines a Square"""

    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        if self.__validate_tuple(position) is False \
                or self.__validate_index(position) is False \
                or self.__validate_integers(position) is False \
                or self.__validate_value(position) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if self.__validate_tuple(position) is False \
                or self.__validate_index(position) is False \
                or self.__validate_integers(position) is False \
                or self.__validate_value(position) is False:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

    def __validate_tuple(self, position):
        if type(position) is tuple:
            return True
        return False

    def __validate_index(self, position):
        if len(position) == 2:
            return True

        return False

    def __validate_integers(self, position):
        if type(position[0]) is int and type(position[1]) is int:
            return True
        return False

    def __validate_value(self, position):
        if position[0] >= 0 and position[1] >= 0:
            return True
        return False

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return None

        if self.__position[1] > 0:
            for y in range(self.__position[1]):
                print('')
        for x in range(1, self.area() + 1):
            if x % self.__size == 1:
                print('{:>{w}}'.format('#', w=self.__position[0] + 1), end='')
            else:
                print('#', end='')

            if x % self.__size == 0 and x > 0:
                print()
