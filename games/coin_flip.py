# Coin flip game

import random

def play():
    # Config
    odds = 0.5 # This is the odds for the coin to land on heads

    # Variables
    player_points = 0
    opponent_points = 0

    # Main game loop
    print("Welcome to Coin Flip!\n") # Intro message
    while True:
        cmd = input("Heads or tails?\n").lower() # Get user input
        if cmd == "quit" or cmd == "exit": # Escape case to quit the game
            print("Leaving \"Coin Flip\"...")
            return # sys.exit("Game closed.")

        if cmd == "heads" or cmd == "tails":
            outcome = random.random()
            if outcome < odds: outcome = "heads"
            else: outcome = "tails"

            if cmd == outcome:
                player_points += 1
                print(f"You win! ({player_points}/{opponent_points})")
            else:
                opponent_points += 1
                print(f"You lose! ({player_points}/{opponent_points})")

if __name__ == "__main__":
    play()