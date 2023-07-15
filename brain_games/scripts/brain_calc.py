#!/usr/bin/env python3

from random import choice
from random import randint
import prompt
import brain_games.cli


def proverka_answer(otvet_user, real_otvet):
    if otvet_user == real_otvet:
        return True
    else:
        return False


def generate_operations():
    oper = ['+', '-', '*']
    return choice(oper)


def calc_rotvet(rand_n1, rand_n2, oper):
    if oper == '+':
        return rand_n1 + rand_n2
    elif oper == '-':
        return rand_n1 - rand_n2
    else:
        return rand_n1 * rand_n2


def main():
    name = brain_games.cli.welcome_user()
    print('What is the result of the expression?')
    i = 0
    success = True
    while i <= 2:
        rand_n1 = randint(1, 100)
        rand_n2 = randint(1, 100)
        oper = generate_operations()
        real_otvet = calc_rotvet(rand_n1, rand_n2, oper)
        print('Question: ' + str(rand_n1) + ' ' + str(oper) + ' ' + str(rand_n2))
        otvet = prompt.string('Your answer: ')
        otvet = int(otvet)
        if proverka_answer(otvet, real_otvet) is True:
            i += 1
            print('Correct')
            continue
        else:
            print("'" + str(otvet) + "' is wrong answer ;(."
                  " Correct answer was " + "'" + str(real_otvet) + "'")
            print("Let's try again, " + name + "!")
            success = False
            break
    if success:
        print("Congratulations, " + name + "!")


if __name__ == '__main__':
    main()
