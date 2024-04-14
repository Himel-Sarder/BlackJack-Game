# Blackjack Game
![BlackJack](https://github.com/Himel-Sarder/BlackJack-Game/assets/143216886/3e8eefcb-3aa2-4103-aa59-3745ea43d7f7)

Welcome to the Blackjack game! This is a command-line implementation of the classic casino game Blackjack, also known as 21. In this game, you'll play against a computerized dealer and aim to beat them by getting as close to 21 points as possible without going over.

## ScreenShots   
![image](https://github.com/Himel-Sarder/BlackJack-Game/assets/143216886/3b322f72-fcbb-4989-b8b7-337aa09e0a71)
![image](https://github.com/Himel-Sarder/BlackJack-Game/assets/143216886/ae787207-f1c3-4d94-b6cd-4782934a3163)
![image](https://github.com/Himel-Sarder/BlackJack-Game/assets/143216886/778f2f00-a306-411a-8405-dccad0c4c537)
![image](https://github.com/Himel-Sarder/BlackJack-Game/assets/143216886/972ba7b5-2668-404c-93b0-02d7aad340bf)
![image](https://github.com/Himel-Sarder/BlackJack-Game/assets/143216886/f9f3664e-1a3c-4c8a-9ae8-b274c27b49f3)
![image](https://github.com/Himel-Sarder/BlackJack-Game/assets/143216886/027e99eb-75ef-4a7c-bcb6-adfa8cf783e1)

## Try it on Replit   
[Click Me](https://replit.com/@AntuSarder/Blackjack-Game)

## Card introduction   
![image](https://github.com/Himel-Sarder/BlackJack-Game/assets/143216886/f1d59f0c-087f-4fcc-8402-97270f92898d)

## Card's value for this game   
In the game of Blackjack, the value of cards is as follows:

- Number cards (2 through 10): Face value (e.g., 2 has a value of 2, 10 has a value of 10).
- Face cards (Jack, Queen, King): Each worth 10 points.
- Ace: Can be counted as either 1 or 11 points, whichever is more advantageous to the player without exceeding 21.

Here's a summary:

- **Number cards:** Face value (2-10)
- **Face cards:** 10 points each (Jack, Queen, King)
- **Ace:** 1 or 11 points

These values are used to calculate the total hand value in the game of Blackjack.

## Features

- **Player vs. Dealer**: Play against the computerized dealer.
- **Hit or Stand**: Choose whether to hit (take another card) or stand (keep your current hand).
- **Blackjack**: Win instantly if you get a Blackjack (an Ace and a 10-value card) on the first two cards.
- **Betting System**: Start with 50 coins. Win 10 coins for each win and lose 10 coins for each loss. If you have fewer than 10 coins, the game ends.
- **Simple User Interface**: Easy-to-understand text-based interface suitable for beginners.
## Game Rules

- **Objective**: The goal is to get a hand value as close to 21 as possible without exceeding it.
- **Card Values**: Number cards are worth their face value, face cards (Jack, Queen, King) are worth 10, and Aces are worth 11 or 1.
- **Blackjack**: A Blackjack is a hand containing an Ace and a 10-value card, totaling 21 points. It's the highest-ranking hand.
- **Busting**: If your hand value exceeds 21 points, you bust and lose the round.
- **Dealer's Turn**: The dealer must hit until their hand value is 17 or higher.

## For Better Understand 
Watch This Video : 
https://www.youtube.com/embed/eyoh-Ku9TCI?si=pL8CAkB-SjfJiWll

Play This online Game : 
https://247blackjack.com/

## How to Play

To play the Blackjack game step by step, follow these instructions:

1. **Start the Game**: Run the Python script `blackjack.py` in your terminal or command prompt. You can do this by navigating to the directory where the script is located and typing `python blackjack.py`.

2. **Game Setup**: Once the game starts, you'll see the initial setup, including your current hand and the dealer's visible card. Follow the prompts to decide whether you want to hit (take another card) or stand (keep your current hand).

3. **Make Your Move**: If you choose to hit, you'll receive another card. If you choose to stand, you'll keep your current hand. Keep making moves until you're satisfied with your hand or until you bust (go over 21).

4. **Dealer's Turn**: After you've made your moves, it's the dealer's turn to play. The dealer will follow a predefined set of rules for hitting or standing. You'll see the dealer's final hand once they've completed their turn.

5. **Determine the Winner**: Once both you and the dealer have finished playing, the winner is determined based on who has the hand closest to 21 without exceeding it. If you have a higher hand value than the dealer without busting, you win. If the dealer has a higher hand value or if you bust, the dealer wins.

6. **Betting**: After each round, your coins will be adjusted based on whether you win or lose. You'll gain 10 coins for each win and lose 10 coins for each loss. If you run out of coins (less than 10), the game will end.

7. **Play Again**: You'll be prompted to decide whether you want to play another round. Type 'yes' to continue playing or 'no' to end the game.

8. **Game Over**: If you choose to end the game or if you run out of coins, the game will end, and you'll see your final coin count.

Follow these steps to play the Blackjack game step by step and enjoy the gameplay experience!
## Betting System

In this game, there's a betting system to add an extra layer of excitement:

- **Initial Coins**: You start with 50 coins.
- **Winning**: Win 10 coins for each win.
- **Losing**: Lose 10 coins for each loss.
- **Game Over**: If you have fewer than 10 coins, the game ends.


## Requirements

- Python 3.x

## Installation

Clone the repository to your local machine:

```
git clone https://github.com/Himel-Sarder/blackjack-game.git
```

## Usage

Navigate to the project directory and run the Python script:

```
cd blackjack-game
python blackjack.py
```

Follow the on-screen prompts to play the game.

## Credits   
- Himel Sarder
- Department of Computer Science and Engineering
- Bangamata Sheikh Fojilatunnesa Mujib Science and Technology University, Jamalpur, Bangladesh
- Linkedin : [Himel Sarder](https://www.linkedin.com/in/himel-sarder/)
- Gmail : [Contact with me](info.himelcse@gmail.com)

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
