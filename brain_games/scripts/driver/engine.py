#!/usr/bin/env python3

from random import choice
from random import randint
import brain_games.scripts
import prompt


def final_output(REAL_ANSWER, NAME):
    USER_ANSWER = prompt.string('Your answer: ')
    if verify_answer(USER_ANSWER, REAL_ANSWER) is False:
        print("'" + str(USER_ANSWER) + "' is wrong answer ;(."
              " Correct answer was '" + str(REAL_ANSWER) + "'.")
        print("Let's try again, " + NAME + "!")
        return False
    else:
        return True


def games_engine(NAME, NAME_GAME):
    games = {
        'brain_even': brain_games.scripts.brain_even.play_brain_even,
        'brain_calc': brain_games.scripts.brain_calc.play_brain_calc,
        'brain_gcd': brain_games.scripts.brain_gcd.play_brain_gcd,
        'brain_progression': brain_games.scripts.brain_progression.play_brain_progression,
        'brain_prime': brain_games.scripts.brain_prime.play_brain_prime
    }
    play_game = games.get(NAME_GAME)
    if not play_game:
        return False
    for _ in range(3):
        if play_game(NAME):
            print('Correct')
        else:
            return False
    return True


def verify_answer(USER_ANSWER, REAL_ANSWER):
    if str(USER_ANSWER) == str(REAL_ANSWER):
        return True
    else:
        return False


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





def calc_nod(r_n1, r_n2):
    nod = 0
    while True:
        nod = r_n1 % r_n2
        r_n1 = r_n2
        if nod == 0:
            return r_n2
        r_n2 = nod


def play_brain_even(name):
    random_num = randint(1, 100)
    print('Question: ' + str(random_num))
    otvet = prompt.string('Your answer: ')
    prov_corr = vopros_otvet(random_num, otvet)
    otvet_vprint = corr_otvet(random_num)
    if prov_corr is False:
        print("'" + str(otvet) + "' is wrong answer ;(."
              " Correct answer was '" + otvet_vprint + "'.")
        print("Let's try again, " + name + "!")
        return False
    else:
        return True





def play_brain_gcd(name):
    rand_n1 = randint(1, 100)
    rand_n2 = randint(1, 100)
    print('Question: ' + str(rand_n1) + ' ' + str(rand_n2))
    real_otvet = calc_nod(rand_n1, rand_n2)
    otvet = prompt.string('Your answer: ')
    prov_corr = verify_answer(otvet, real_otvet)
    otvet_vprint = str(real_otvet)
    if prov_corr is False:
        print("'" + str(otvet) + "' is wrong answer ;(."
              " Correct answer was '" + otvet_vprint + "'.")
        print("Let's try again, " + name + "!")
        return False
    else:
        return True


def play_brain_progression(name):
    q_chisl = randint(5, 15)
    num_otvet = randint(1, q_chisl)
    shag = randint(2, 7)
    real_otvet = vivod_posled(q_chisl, num_otvet, shag)
    otvet = prompt.string('Your answer: ')
    prov_corr = verify_answer(otvet, real_otvet)
    otvet_vprint = str(real_otvet)
    if prov_corr is False:
        print("'" + str(otvet) + "' is wrong answer ;(."
              " Correct answer was '" + otvet_vprint + "'.")
        print("Let's try again, " + name + "!")
        return False
    else:
        return True


def play_brain_prime(name):
    random_num = randint(1, 100)
    print('Question: ' + str(random_num))
    otvet = prompt.string('Your answer: ')
    otvet_vprint = otvet_prostoe(random_num)
    prov_corr = prover_prostoe(otvet_vprint, otvet)
    if prov_corr is False:
        print("'" + str(otvet) + "' is wrong answer ;(."
              " Correct answer was '" + otvet_vprint + "'.")
        print("Let's try again, " + name + "!")
        return False
    else:
        return True


def otvet_prostoe(random_num):
    if random_num < 2:
        return 'no'
    for i in range(2, random_num // 2 + 1):
        if random_num % i == 0:
            return 'no'
    return 'yes'


def prover_prostoe(otvet_vprint, otvet):
    if otvet_vprint == otvet:
        return True
    else:
        return False


def vivod_posled(q_chisl, num_otvet, shag):
    perv_ch = randint(1, 100)
    posled = ''
    i = 1
    real_otvet = perv_ch + shag
    while i <= q_chisl:
        if i == num_otvet:
            posled += '..'
            real_otvet = perv_ch + shag
        else:
            posled += str(perv_ch + shag)
        if i < q_chisl:
            posled += ' '
        perv_ch = perv_ch + shag
        i += 1
    posled = 'Question: ' + posled
    print(posled)
    return real_otvet
