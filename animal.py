
import sys
def dog():
    print(‘Baw')


import sys

def cat():
    print('Meow')


def default():
    print('Hello')

def main():


    if sys.argv[1] == ‘dog':
        dog()
    else:
    default()

    if sys.argv[1] == 'cat':
        cat()
    else:
        default()


if __name__ == '__main__':
    main()

