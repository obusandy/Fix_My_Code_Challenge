#!/usr/bin/python3
""" Square class"""


class Square():
    """ Square class instance
    width and height initialization"""
    width = 0
    height = 0
    def __init__(self, *args, **kwargs):
        """ Arguments:
        key, value"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square 
        width multiplied by height"""
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Perimeter distance of the specific square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ display results """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    """ main point of entry """
    sqe = Square(width=12, height=9)
    print(sqe)
    print(sqe.area_of_my_square())
    print(sqe.permiter_of_my_square())