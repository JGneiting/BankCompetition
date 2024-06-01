import sys
import os

import argparse

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.game import LocalGame, get_entries  # noqa: E402

if __name__ == "__main__":
    # Add the src directory to sys.path

    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("num_games", help="The number of games.\n", type=int, default=1)

    arg_parser.add_argument("num_rounds", help="The number of rounds.\nOptions are: [10, 15, 20]",
                            type=int, choices=[10, 15, 20], default=10)

    # search the entries directory for python files. Try to import a "main" function
    entries = []
    wins = {}
    exclude = ["__init__.py", "test.py", "the_leech.py"]
    entries = get_entries("src/entries", exclude)

    for entry in entries:
        wins[entry.name] = 0

    # run the game

    for _ in range(arg_parser.parse_args().num_games):
        game = LocalGame(arg_parser.parse_args().num_rounds, *entries)
        game.run()
        winner = game.get_winner()
        wins[winner.name] += 1

    print(wins)
