#!/usr/bin/python3
"""
Text indentation
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    try:
        new_text = ""
        indentation = [".", "?", ":"]
        for i in text:
            if i is " " and new_text is "":
                continue
            new_text += i
            if i in indentation:
                print(new_text + "\n")
                new_text = ""
        print(new_text, end="")
    except TypeError:
        raise TypeError("text must be a string")

if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/5-text_indentation.txt")
