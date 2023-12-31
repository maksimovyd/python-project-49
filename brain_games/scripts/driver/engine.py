#!/usr/bin/env python3

import brain_games.scripts
import brain_games.scripts.brain_even
import brain_games.scripts.brain_calc
import brain_games.scripts.brain_gcd
import brain_games.scripts.brain_progression
import brain_games.scripts.brain_prime
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
        'brain_progression': (
            brain_games.scripts.brain_progression.play_brain_progression),
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
    return str(USER_ANSWER) == str(REAL_ANSWER)
