from time import time

def connect() -> None:
    print('Connecting to the internet...')
    print('You are connected!')


def greet() -> None:
    return('Hello World!')

def bye() -> None:
    print('Bye World!')


def main() -> None:
    greet()
    bye()

if __name__ == '__main__':
    main()


