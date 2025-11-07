# Rock, Paper, Scissors Game

import random

def play():
    # Variables
    player_points = 0
    opponent_points = 0

    # TODO: Make enum for rock/paper/scissors strings to avoid magic strings?

    def get_opponent_move():
        move = random.randint(0, 2)
        if move == 0: return "rock"
        elif move == 1: return "paper"
        elif move == 2: return "scissors"
        return None # TODO: Have this throw an exception instead

    def wins_against(m1, m2): # Boolean
        return ((m1 == "rock" and m2 == "scissors")
                or (m1 == "paper" and m2 == "rock")
                or (m1 == "scissors" and m2 == "paper"))

    # Main game loop
    print("Welcome to Rock Paper Scissors!\n") # Intro message
    while True:
        cmd = input("What move? (rock, paper, scissors)\n").lower() # Get user input
        if cmd == "quit" or cmd == "exit": # Escape case to quit the game
            print("Leaving \"Rock Paper Scissors\"...")
            return # sys.exit("Game closed.")

        opponent_move = get_opponent_move()
        if cmd == "rock" or cmd == "paper" or cmd == "scissors":
            print("You played " + cmd + ".")
            print("The opponent played " + opponent_move + "!")

            if cmd == opponent_move: # The player and opponent tie this round
                print("Tie! (" + str(player_points) + "/" + str(opponent_points) + ")")

            elif wins_against(cmd, opponent_move): # The player wins this round
                player_points += 1
                print("You win! (" + str(player_points) + "/" + str(opponent_points) + ")")

            else: # The player loses this round
                opponent_points += 1
                print("You lose! (" + str(player_points) + "/" + str(opponent_points) + ")")

            print("\n")
        else: print("You can only play 'rock', 'paper', or 'scissors'!")

if __name__ == "__main__":
    play()