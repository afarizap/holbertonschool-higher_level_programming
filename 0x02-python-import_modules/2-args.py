#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    if argc == 1:
        print("{:d} argument:".format(argc))
    else:
        print("{:d} arguments.".format(argc))
    x = 0
    for i in range(argc):
        print("{:d}: {:s}".format(i + 1, str(sys.argv[i + 1])))
