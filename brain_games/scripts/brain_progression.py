#!/usr/bin/env python3

from brain_games.engine import engine
from brain_games.games.progression import progression_game
from brain_games.games.progression import RULES


def main():
    engine(progression_game, RULES)


if __name__ == '__main__':
    main()
