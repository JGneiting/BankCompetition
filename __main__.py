import sys
import os

import argparse

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from BankCompetition.bankcompetition.src.bankcompetition.game import LocalGame, get_entries  # noqa: E402

if __name__ == "__main__":
    # Add the src directory to sys.path

    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("num_games", help="The number of games.\n", type=int, default=1)

    arg_parser.add_argument("num_rounds", help="The number of rounds.\nOptions are: [10, 15, 20]",
                            type=int, choices=[10, 15, 20], default=10)
    arg_parser.add_argument("-m", "--manual", help="Enable manual mode.\n", action="store_true", default=False)

    args = arg_parser.parse_args()

    # search the entries directory for python files. Try to import a "main" function
    entries = []
    wins = {}
    ties = {}
    scores = {}
    total_scores = {}
    average_scores = {}
    median_scores = {}
    exclude = ["__init__.py", "test.py"]
    if not args.manual:
        exclude.append("manual.py")
    entries = get_entries("src/entries", exclude)

    for entry in entries:
        wins[entry.name] = 0
        ties[entry.name] = 0
        scores[entry.name] = 0
        total_scores[entry.name] = 0
        median_scores[entry.name] = []

    # run the game

    for _ in range(args.num_games):
        game = LocalGame(args.num_rounds, *entries)
        game.run()
        winners = game.get_winner()
        if len(winners) == 1:
            wins[winners[0].name] += 1
            scores[winners[0].name] += 1
        elif len(winners) >= 0:
            for winner in winners:
                ties[winner.name] += 1
                scores[winner.name] += 0.5
        for player in game.state.players:
            total_scores[player.name] += player.score
            median_scores[player.name].append(player.score)

    for entry in entries:
        average_scores[entry.name] = total_scores[entry.name] / arg_parser.parse_args().num_games
        median_scores[entry.name] = sorted(median_scores[entry.name])[len(median_scores[entry.name]) // 2]

    print("Wins: ", wins)
    print("Ties: ", ties)
    print("Scores: ", scores)
    # print("Total Scores: ", total_scores)
    print("Average Scores: ", average_scores)
    # print("Median Scores: ", median_scores)
