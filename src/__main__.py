import os
import argparse

from game import Game


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("num_rounds", help="The number of rounds.\nOptions are: [10, 15, 20]",
                            type=int, choices=[10, 15, 20], default=10)

    # search the entries directory for python files. Try to import a "main" function
    entries = []
    for entry_file in os.listdir("src/entries"):
        if entry_file.endswith(".py") and entry_file != "__init__.py":
            try:
                # Import the module dynamically
                module_name = entry_file[:-3]  # Strip ".py" extension
                module = __import__(f"entries.{module_name}", globals(), locals(), ["main"])

                # Check if the module has a main function
                if hasattr(module, "main"):
                    # Call the main function with the name derived from the file path
                    entry_name = module_name.capitalize()  # or use any other naming convention
                    entry_instance = module.main(entry_name)
                    entries.append(entry_instance)
            except Exception as e:
                print(f"Failed to import entry {entry_file}:", e)

    # run the game
    game = Game(arg_parser.parse_args().num_rounds, *entries)
    game.run()
