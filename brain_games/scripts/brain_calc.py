#!/usr/bin/env python3

from brain_games.engine import engine
from brain_games.games.calc import calc_game
from brain_games.games.calc import RULES


def launch_calc_game():
    engine(calc_game, RULES)
