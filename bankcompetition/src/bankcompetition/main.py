import argparse
from .game import get_entries, LocalGame


def main() -> None:
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("num_rounds", help="The number of rounds.\nOptions are: [10, 15, 20]",
                            type=int, choices=[10, 15, 20], default=10)

    # search the entries directory for python files. Try to import a "main" function
    entries = []
    exclude = ["__init__.py", "test.py", "gradient.py"]
    entries = get_entries("entries", exclude)

    print(entries)

    # run the game
    game = LocalGame(arg_parser.parse_args().num_rounds, *entries)
    game.run()
