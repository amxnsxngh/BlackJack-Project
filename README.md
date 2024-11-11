BlackJack Game
This is a simple Python-based implementation of the classic BlackJack card game. The game allows a user to play against the computer, dealing cards and calculating scores according to BlackJack rules.

Features:
Card Dealing: Each player is dealt two cards at the start of the game.
Blackjack Check: If either the player or the computer has an Ace and a 10-point card, they win with a Blackjack.
Card Drawing: The player has the option to draw more cards until they either choose to stop or their score exceeds 21.
Ace Handling: If the player or computer has an Ace (valued at 11), it is automatically adjusted to 1 if the score exceeds 21.
Computer AI: The computer continues drawing cards until its score is at least 17.
Game Outcome: The game checks if the player or computer wins based on their final hand values, including handling cases of tie (draw), Blackjack, or exceeding 21 (bust).
How to Play:
Upon running the game, you will be prompted to decide whether to play the game or not by typing 'y' (yes) or 'n' (no).

If you choose to play:

You will be shown your cards and the computer's first card.
If you have a Blackjack (a hand with an Ace and a 10), you win automatically.
You can keep drawing cards by typing 'y' to improve your score or 'n' to stop.
If your score exceeds 21, you lose automatically.
The computer will draw cards until its score is 17 or higher.
If the player's score is higher than the computer’s without exceeding 21, the player wins. Otherwise, the computer wins or the game ends in a draw.
After the round, you can choose to play again or exit by typing 'y' or 'n' when prompted.

