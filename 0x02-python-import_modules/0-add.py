#!/usr/bin/python3
import add_0 as add


def main():
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add.add(a, b)))


if __name__ == '__main__':
    main()
