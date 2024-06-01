import os
import argparse

from game import Game
from entry import Entry


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("num_rounds", help="The number of rounds.\nOptions are: [10, 15, 20]", type=int, choices=[])

    # search the entries directory for python files. Try to import a "main" function
    entries = []
    for entry in os.listdir("entries"):
        if entry.endswith(".py") and entry != "__init__.py":
            try:
                module = __import__(f"entries.{entry[:-3]}", globals(), locals(), ["main"])
                if hasattr(module, "main"):
                    entries.append(Entry(entry[:-3], module.main))
            except Exception as e:
                print(f"Failed to import entry {entry}:", e)

    # run the game
    game = Game(10, *entries)
