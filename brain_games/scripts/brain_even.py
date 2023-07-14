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


def main():
    name = brain_games.cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    success = True
    while i <= 2:
        random_num = randint(1, 100)
        print('Question: ' + str(random_num))
        otvet = prompt.string('Your answer: ')
        if vopros_otvet(random_num, otvet) == True:
            i += 1
            print('Correct')
            continue
        elif vopros_otvet(random_num, otvet) == False and otvet == 'no':
            print("'" + otvet + "' is wrong answer ;(. Correct answer was 'yes'.")
            print("Let's try again, " + name + "!")
            success = False
            break
        else:
            print("'" + otvet + "' is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again, " + name + "!")
            success = False
            break
    if success:
        print("Congratulations, " + name + "!")


if __name__ == '__main__':
    main()
