#!/usr/bin/env python3

from random import randint
import prompt
import brain_games.cli


def proverka_chetnosty(chislo):
    if chislo % 2 == 0:
        return True
    else:
        return False


def vopros_otvet(random_num, otvet):
    prav_otvet = random_num % 2
    if otvet == 'yes' and prav_otvet == 0:
        return True
    elif otvet == 'no' and prav_otvet == 1:
        return True
    else:
        return False


def corr_otvet(random_num):
    if proverka_chetnosty(random_num) is True:
        return 'yes'
    else:
        return 'no'


def main():
    name = brain_games.cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    success = True
    while i <= 2:
        random_num = randint(1, 100)
        print('Question: ' + str(random_num))
        otvet = prompt.string('Your answer: ')
        if vopros_otvet(random_num, otvet) is True:
            i += 1
            print('Correct')
            continue
        else:
            print("'" + otvet + "' is wrong answer ;(."
                  " Correct answer was '" + corr_otvet(random_num) + "'.")
            print("Let's try again, " + name + "!")
            success = False
            break
    if success:
        print("Congratulations, " + name + "!")


if __name__ == '__main__':
    main()
