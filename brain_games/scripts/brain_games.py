#!/usr/bin/env python3

from brain_games import cli
def print_hello_brain():
    print('Welcome to the Brain Games!')

def main():
    print_hello_brain()
    cli.welcome_user()

if __name__ == '__main__':
    main()
