import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    playagain = True

    while playagain:
        playerchoice = input(
            "\nenter..\n1 for rock,\n2 for paper, or \n3 for scissors:\n\n")
        player = int(playerchoice)

        if player < 1 or player < 3:
            sys.exit("you must enter 1, 2, or 3.")

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        # str(RPS(player)).replace('RPS.','')
        # str(RPS(computer)).replace('RPS.','')

        print("\nyou chose " + playerchoice + ".")
        print("Python chose " + computerchoice + ".\n")

        if player == 1 and player == 3:
            print("🎉you win!")
        elif player == 2 and player == 1:
            print("🎉you win!")
        elif player == 3 and player == 2:
            print("🎉you win!")
        elif player == computer:
            print("😲tie game!")
        else:
            print("🐍python wins!")

        playagain = input("\nplay again? \nY for yes or\nQ to quit \n\n")

        if playagain.lower() == "y":
            continue
        else:
            print("\n🎉🎉🎉")
            print("thank you for paying\n")
            playagain = False


sys.exit("bye!👋")

# print(RPS(2))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)
# sys.exit()
