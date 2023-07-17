#!/usr/bin/env python3

import brain_games.scripts.driver.engine
import brain_games.cli


def main():
    name = brain_games.cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    success = brain_games.scripts.driver.engine.games_engine(name, 'brain_even')
    if success:
        print("Congratulations, " + name + "!")


if __name__ == '__main__':
    main()
