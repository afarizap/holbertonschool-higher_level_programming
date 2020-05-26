#!/usr/bin/python3
def magic():
    a = "HBTN"
    b = "HBTN"
    del a
    del b
    c = "HBTN"
if __name__ == "__main__":
    import dis
    dis.dis(magic)
