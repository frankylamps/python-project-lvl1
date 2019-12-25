#!/usr/bin/env python3

from brain_games.engine import engine
from brain_games.games.prime import prime_game
from brain_games.games.prime import RULES


def main():
    engine(prime_game, RULES)


if __name__ == '__main__':
    main()
