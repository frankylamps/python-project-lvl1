#!/usr/bin/env python3

from brain_games.engine import engine
from brain_games.games.progression import progression_game
from brain_games.games.progression import RULES


def launch_progression_game():
    engine(progression_game, RULES)
