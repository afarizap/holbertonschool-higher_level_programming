#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    x = 0
    for i in range(argc):
        x += int(sys.argv[i + 1])
    print("{:d}".format(x))
