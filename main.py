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
    input("\nPress Enter to roll the dice...🎲 🎲")

    # Player dice
    player_dice1 = random.randint(1,6)
    player_dice2 = random.randint(1,6)
    player_total = player_dice1 + player_dice2

    # Computer dice
    computer_dice1 = random.randint(1,6)
    computer_dice2 = random.randint(1,6)
    computer_total = computer_dice1 + computer_dice2

    print("\nYou rolled:", dice[player_dice1], "and", dice[player_dice2])
    print("Your total:", player_total)

    print("\nComputer rolled:", dice[computer_dice1], "and", dice[computer_dice2])
    print("Computer total:", computer_total)

    if player_total > computer_total:
        print("You win this round! ")
        player_score += 1

    elif player_total < computer_total:
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