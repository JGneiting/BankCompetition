# BANK Competition

Welcome to the BANK competition! This project is a competitive game where participants create agents that play the game "BANK". Below you will find the rules of the game, how to create and submit an agent, and how to participate in the competition.

## Game Rules

1. **Gameplay**
    - The game consists of 20 rounds.
    - Players take turns rolling two standard six-sided dice during each round.

2. **Scoring**
    - Players may choose to 'Bank' at any time, which adds the current round's score to their total score and ends the round.
    - During the first three rolls of a round:
        - Rolling a 7 adds 70 points to the round's score.
        - Any other number adds its face value to the round's score.
    - From the 4th roll onward:
        - Rolling doubles doubles the round's score.
        - Rolling a 7 ends the round with zero points added to the total score.
        - Any other number adds its face value to the round's score.

3. **Winning**
    - The player with the highest score at the end of 20 rounds wins the game.

## Creating an Agent

1. **Installing**
    First, you need to install the bank competition package. to do this, run the following command
    ```bash
     pip install git+https://github.com/JGneiting/BankCompetition.git@main#egg=bankcompetition&subdirectory=bankcompetition
     ```
2. **Creating your Agent**
   To create an agent, start with the base class provided. You cannot remove the bank function but are free to make any other modifications to make your agent work.
   ```python
   from bankcompetition.entry import Entry


    class TestEntry(Entry):
        def __init__(self, name: str):
            super().__init__(name)
    
        def bank(self, state) -> bool:
            return True
    
    
    def main(name: str) -> Entry:
        return TestEntry(name)
   ```
3. **Uploading your Agent**
   To upload your agent, first visit the [competition website](https://bakerbot3000.com/bankcompetition/) and create an account. From here, you can upload agents from your dashboard. You need to have the starter code inside a file titled ```main.py```. Have any other python files or data in the same folder, and upload the entire folder to the server. If there are no issues and validation passes, your entry has been successfully submitted and will compete in the next competition!

## How to Contribute

1. Fork the repository.
2. Clone your forked repository.
3. Create your agent in the 'agents' directory.
4. Test your agent by running it locally.
5. Submit a pull request with your agent.

We look forward to your participation and hope you enjoy the game!

For any questions or issues, please open an issue in the repository or contact the competition organizers.

Happy banking!
