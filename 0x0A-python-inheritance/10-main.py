#!/usr/bin/python3
Square = __import__('10-square').Square


s = Square(13)


print(s)
print(s.area())
print(issubclass(Square, Rectangle))
try:
    s = Square(13)
    print(s.size)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
try:
    s = Square("13")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
