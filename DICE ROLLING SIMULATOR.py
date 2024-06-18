import random

def roll_dice():
    return random.randint(1, 6)

def dice_rolling_simulator():
    user_wins = 0
    computer_wins = 0

    while user_wins < 2 and computer_wins < 2:
        user_roll = roll_dice()
        computer_roll = roll_dice()
        print(f"You rolled: {user_roll}")
        print(f"Computer rolled: {computer_roll}")

        if user_roll > computer_roll:
            user_wins += 1
            print("You win this round!")
        elif user_roll < computer_roll:
            computer_wins += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")

    if user_wins == 2:
        print("You win the game!")
    else:
        print("Computer wins the game!")

dice_rolling_simulator()