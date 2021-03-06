
#!/usr/bin/python3
class Square:
    """Square class that calculates the area of
    a sqare, has a getter and setter method"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        i = 0
        j = 0
        if self.__size == 0:
            print()
        else:
            while (i < self.__size):
                j = 0
                while (j < self.__size):
                    print("#", end='')
                    j += 1
                print()
                i += 1
