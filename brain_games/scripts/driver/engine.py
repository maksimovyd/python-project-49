#!/usr/bin/env python3

from random import choice
from random import randint
import prompt


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


def games_engine(name, name_game):
    otvet_vprint = ''
    prov_corr = False
    i = 0
    while i <= 2:
        if name_game == 'brain_even':
            random_num = randint(1, 100)
            print('Question: ' + str(random_num))
            otvet = prompt.string('Your answer: ')
            prov_corr = vopros_otvet(random_num, otvet)
            otvet_vprint = corr_otvet(random_num)
        elif name_game == 'brain_calc':
            rand_n1 = randint(1, 100)
            rand_n2 = randint(1, 100)
            oper = generate_operations()
            real_otvet = calc_rotvet(rand_n1, rand_n2, oper)
            print('Question: ' + str(rand_n1) + ' ' + str(oper) +
                  ' ' + str(rand_n2))
            otvet = prompt.string('Your answer: ')
            otvet = int(otvet)
            prov_corr = proverka_answer(otvet, real_otvet)
            otvet_vprint = str(real_otvet)
        if prov_corr is True:
            i += 1
            print('Correct')
            continue
        else:
            print("'" + str(otvet) + "' is wrong answer ;(."
                  " Correct answer was '" + otvet_vprint + "'.")
            print("Let's try again, " + name + "!")
            return False
    return True
