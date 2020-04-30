#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        if len(sys.argv) == 2:
            print("1 argument:")
            print("1: {:s}".format(str(sys.argv[1])))
        else:
            print("{:d} arguments:".format(len(sys.argv)))
            for i in range(len(sys.argv)):
                print("{:d}: {:s}".format(i, str(sys.argv[i])))
