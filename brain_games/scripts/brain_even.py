#!/usr/bin/env python3

from brain_games.engine import engine
from brain_games.games.even import even_game
from brain_games.games.even import RULES


def main():
    engine(even_game, RULES)


if __name__ == '__main__':
    main()
