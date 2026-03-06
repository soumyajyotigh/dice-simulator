import random
dice = {
1: "[⚀]",
2: "[⚁]",
3: "[⚂]",
4: "[⚃]",
5: "[⚄]",
6: "[⚅]"
}
player_score = 0
computer_score = 0

print("Welcome to the Dice Game!")

while True:
    input("\nPress Enter to roll the dice...")

    player_roll = random.randint(1,6)
    computer_roll = random.randint(1,6)

    print("You rolled:", dice[player_roll])
    print("Computer rolled:", dice[computer_roll])

    if player_roll > computer_roll:
        print("You win this round! ")
        player_score += 1

    elif player_roll < computer_roll:
        print("Computer wins this round! ")
        computer_score += 1

    else:
        print("It's a tie!")

    print("\nScore:")
    print("You:", player_score)
    print("Computer:", computer_score)

    choice = input("\nPlay again?")

    if choice.lower() not in ['yes', 'y']:
        print("\nFinal Score")
        print("You:", player_score)
        print("Computer:", computer_score)
        print("Thanks for playing! 🎲")
        break