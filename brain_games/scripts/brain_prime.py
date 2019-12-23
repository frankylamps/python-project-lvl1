#!/usr/bin/env python3

from brain_games.engine import engine
from brain_games.games.prime import prime_game
from brain_games.games.prime import RULES


def launch_prime_game():
    engine(prime_game, RULES)
