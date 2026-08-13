# rock-paper-scissors
play game
# Rock Paper Scissors Game 🎮

## About the Project

This is a simple **Rock Paper Scissors game developed using Python**.

The player can choose:

* `r` → Rock
* `p` → Paper
* `s` → Scissors
* `999` → Exit the game

The computer randomly selects Rock, Paper, or Scissors. The program compares the player's choice with the computer's choice and updates the scores.

The game continues until the player enters `999`.

## How the Game Works

### 1. Import Random Module

The `random` module is imported to allow the computer to randomly select Rock, Paper, or Scissors.

```python
import random
```

### 2. Store the Choices

The choices are stored in a list:

```python
rule = ["r", "p", "s"]
```

Here:

* `r` represents Rock
* `p` represents Paper
* `s` represents Scissors

### 3. Display the Instructions

The program displays the available choices to the player before starting the game.

The player can enter `999` to exit the game.

### 4. Rock Function

The `rock()` function is called when the player chooses Rock.

The function checks the computer's choice:

* Rock vs Rock → No one wins
* Rock vs Scissors → Player wins
* Rock vs Paper → Bot wins

The player and bot scores are updated accordingly.

### 5. Paper Function

The `paper()` function is called when the player chooses Paper.

The function checks the computer's choice:

* Paper vs Paper → No one wins
* Paper vs Rock → Player wins
* Paper vs Scissors → Bot wins

The scores are updated after each round.

### 6. Scissors Function

The `scissors()` function is called when the player chooses Scissors.

The function checks the computer's choice:

* Scissors vs Scissors → No one wins
* Scissors vs Paper → Player wins
* Scissors vs Rock → Bot wins

The scores are updated accordingly.

### 7. Global Variables

The variables `player_win` and `bot_win` are used to store the scores.

They are declared as global inside the functions because the functions need to update their values.

```python
global player_win
global bot_win
```

### 8. While Loop

A `while True` loop is used to keep the game running.

During every round:

1. The computer randomly selects a choice.
2. The player enters a choice.
3. The program checks the player's choice.
4. The appropriate function is called.
5. The score is updated.

The loop continues until the player enters `999`.

### 9. Exit Option

The player can stop the game by entering:

```text
999
```

The `break` statement is used to exit the `while` loop.

### 10. Invalid Input

If the player enters anything other than `r`, `p`, `s`, or `999`, the program displays:

```text
please choose between r,p,s only
```

This tells the player to enter a valid choice.

## Final Score

After the player exits the game, the program displays the final scores:

```text
your final scores : player=3    bot=2
```

The program then compares both scores.

### Winner Conditions

* If the player has a higher score → **Player wins**
* If the bot has a higher score → **Bot wins**
* If both scores are equal → **Both have equal scores**

Finally, the program displays:

```text
THANK YOU FOR PLAYING THE GAME
```

## Concepts Used

This project uses the following Python concepts:

* Importing modules
* `random.choice()`
* Lists
* Variables
* Functions
* Global variables
* `if-elif-else`
* `while` loop
* `break` statement
* User input
* String comparison
* Incrementing variables
* Conditional statements

## How to Run the Project

### Requirements

* Python 3.x
* Any Python-supported IDE such as VS Code

### Run the Program

Save the Python file, for example:

```text
rock_paper_scissors.py
```

Then run:

```bash
python rock_paper_scissors.py
```

## Example

```text
for choosing you can select the numbers
rock = 'r'
paper = 'p'
scissor = 's'
exit = 999

enter your choice : r
bot choosen : s
player won the round
score : player=1 bot=0

enter your choice : 999

your final scores : player=1 bot=0
player won the game

THANK YOU FOR PLAYING THE GAME
```

## Future Improvements

The project can be improved by:

* Adding multiple game modes.
* Allowing the player to choose a fixed number of rounds.
* Improving the user interface.
* Adding a graphical interface.
* Adding statistics such as total rounds and win percentage.
