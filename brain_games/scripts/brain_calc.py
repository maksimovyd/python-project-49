#!/usr/bin/env python3

import brain_games.cli
import brain_games.scripts.driver.engine

def main():
    name = brain_games.cli.welcome_user()
    print('What is the result of the expression?')
    success = brain_games.scripts.driver.engine.games_engine(name, 'brain_calc')
    if success:
        print("Congratulations, " + name + "!")


if __name__ == '__main__':
    main()
