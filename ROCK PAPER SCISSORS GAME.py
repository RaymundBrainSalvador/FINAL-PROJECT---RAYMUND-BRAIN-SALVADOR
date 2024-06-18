import random
print("THIS GAME IS FOLLOWING THE BEST OF 3 FORMAT")
def rock_paper_scissors():
    choices = ["rock", "paper", "scissor"]
    user_wins = 0
    computer_wins = 0

    while user_wins < 2 and computer_wins < 2:
        user_choice = input("Choose rock, paper, or scissor: ").lower().strip()
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissor") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissor" and computer_choice == "paper"):
            user_wins += 1
            print("You win this round!")
        else:
            computer_wins += 1
            print("Computer wins this round!")

    if user_wins == 2:
        print("You won the game!")
    else:
        print("Computer won the game!")

rock_paper_scissors()