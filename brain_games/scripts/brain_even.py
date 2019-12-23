#!/usr/bin/env python3

from brain_games.engine import engine
from brain_games.games.even import even_game
from brain_games.games.even import RULES


def launch_even_game():
    engine(even_game, RULES)
