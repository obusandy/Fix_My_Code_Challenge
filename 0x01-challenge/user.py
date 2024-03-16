#!/usr/bin/python3
""" 
User class to encapsulate user information, focusing
on email validation and data security.
"""

class User():
    """ Documentation """

    def __init__(self):
        """ Documentation """
        self.__email = None

    @property
    def email(self):
        """ Documentation 
        initializes an user obj with an empty email add"""
        return self.__email

    @email.setter
    def email(self, value):
        """ Documentation """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value

  
    
if __name__ == "__main__":
    """Main point of entry"""

    usserr = User()
    usserr.email = "john@snow.com"
    print(usserr.email)