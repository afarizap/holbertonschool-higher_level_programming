#!/usr/bin/python3
""" class MyList that inherits from list """


class MyList(list):
    """ class MyList """

    def print_sorted(self):
        """ print the list """
        print(sorted(self))

if __name__ == "__main__":
    import doctest

    doctest.testfile("./tests/1-my_list.txt")
