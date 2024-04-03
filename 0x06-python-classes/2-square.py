#!/usr/bin/python3
"""square module."""


class square:
    """Defines a aquare."""

    def __int__(self, size):
        """Constructor.

        Args:
            size: Length of side of the square.
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise TypeError('size must be >= 0')
        self.__size = size
