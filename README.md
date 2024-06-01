# BANK Competition

Welcome to the BANK competition! This project is a competitive game where participants create agents that play the game "BANK". Below you will find the rules of the game, how to create and submit an agent, and how to participate in the competition.

## Game Rules

1. **Gameplay**
    - The game consists of 20 rounds.
    - Players take turns rolling dice during each round.

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

To participate in the competition, you must create an agent. Your agent will be a Python class that inherits from a base class located in the 'agents' directory. The agent must override the `decision` function, which will be called with the game state and must return a boolean indicating whether the player wishes to bank or not.

### Example Agent

Here is a simple example of an agent:

```python
# agents/simple_agent.py

from base_agent import BaseAgent

class SimpleAgent(BaseAgent):
    def decision(self, game_state):
        # Implement your decision logic here
        # For example, bank if the current round's score is higher than 100
        if game_state['current_round_score'] > 100:
            return True
        return False
```

### Game State

The `decision` function receives the game state as a dictionary. The exact structure of this dictionary will be provided in the base class documentation.

## Entering the Competition

To enter the competition, run your agent on your local machine and connect to the competition URL:

```
https://bakerbot3000/bankcompetition/enter
```

Other agents will connect to this URL as well, and the server will be responsible for running the game and keeping track of scores.

## Repository Structure

```
/agents           # Directory containing agent implementations
    /base_agent.py  # Base agent class to be inherited by participant agents
    /simple_agent.py # Example agent
/README.md         # This README file
```

## How to Contribute

1. Fork the repository.
2. Clone your forked repository.
3. Create your agent in the 'agents' directory.
4. Test your agent by running it locally.
5. Submit a pull request with your agent.

We look forward to your participation and hope you enjoy the game!

For any questions or issues, please open an issue in the repository or contact the competition organizers.

Happy banking!
