import sys

from PyTest1.insofee.myapp.app import divide_by_two, multiply_by_two


def main():
    num = int(input('insert a number'))
    print(f"two of the number is {multiply_by_two(num)}")
    print(f"number when divided by two is {divide_by_two(num)}")
    sys.exit(0)


if __name__ == '__main__':
    main()
