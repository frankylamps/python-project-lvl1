#!/usr/bin/env python3

from brain_games.engine import engine
from brain_games.games.gcd import gcd_game
from brain_games.games.gcd import RULES


def main():
    engine(gcd_game, RULES)


if __name__ == '__main__':
    main()
