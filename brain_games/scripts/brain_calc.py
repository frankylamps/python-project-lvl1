#!/usr/bin/env python3

from brain_games.engine import engine
from brain_games.games.calc import calc_game
from brain_games.games.calc import RULES


def main():
    engine(calc_game, RULES)


if __name__ == '__main__':
    main()
