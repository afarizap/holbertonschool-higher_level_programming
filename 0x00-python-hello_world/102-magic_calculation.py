#!/usr/bin/python3
def magic_calculation(a, b):
    return 98 + a ** b
if __name__ == '__main__':
    import dis
    dis.dis(magic_calculation)
