import sys
import random
from enum import Enum


def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            "\nEnter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n"
        )

        if playerchoice not in ["1", "2", "3"]:
            print("You must enter 1, 2 or 3.")
            return play_rps()

        player = int(playerchoice)

        if player < 1 or player > 3:
            sys.exit("You must enter 1,2, or 3.")

        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print(f"\nYou chose {str(RPS(player)).replace("RPS.", "")}.")
        print(f"Python chose {str(RPS(computer)).replace("RPS.", "")}.\n")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return "🎉You win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "🎉You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "🎉You win!"
            elif player == computer:
                return "😊Tie game!"
            else:
                python_wins += 1
                return "🐍 Python win!"

        game_result = decide_winner(player, computer)

        print(game_result)
        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {str(game_count)}")
        print(f"\nPlayer wins: {str(player_wins)}")
        print(f"\nPython wins:  {str(python_wins)}")

        print("\nPlay agains?")

        while True:
            playgain = input("\nY for Yes or \nQ to Quit\n")
            if playgain.lower() not in ["y", "q"]:
                continue
            else:
                break
        if playgain.lower() == "y":
            return play_rps()
        else:
            print("Thank you for playing!\n")
            sys.exit("Bye! 👌")

    return play_rps


rock_paper_scissors = rps()

if __name__ == "__main__":
    rock_paper_scissors()
