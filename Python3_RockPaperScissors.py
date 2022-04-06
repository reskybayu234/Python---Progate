# Define print_hand function
import utils
import random
print("Starting the Rock Paper Scissors game!")
def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

def judge(player, computer):
    if player == computer:
        return "Draw"
    elif player == 0 and computer == 1:
        return "Lose"
    elif player == 1 and computer == 2:
        return "Lose"
    elif player == 2 and computer == 0:
        return "Lose"
    else:
        return "Win"

def print_hand(hand, name):
    hands = ['Rock','Paper','Scissors']
    print(name + " picked: " + hands[hand])
player_name = input("Please enter your name: ")

print("Pick a hand: (0:Rock, 1:Paper, 2:Scissors)")

player_hand = int(input("Please enter a number (0-2): "))

if utils.validate(player_hand):
    computer_hand = random.randint(0,2)

    utils.print_hand(computer_hand, "computer")

    utils.print_hand(player_hand, player_name)

    result = utils.judge(player_hand, computer_hand)
    print("Result: " + result)
else:
    print("Please enter a valid number!")