import random

choices = ['Rock', 'Paper', 'Scissors'] #the game choices

while True:
    player_choice = input("Choose Rock, Paper, Scissors (or 'quit' to stop): ").capitalize() #capitalize the user input
    if player_choice == 'Quit': #quit the game if the user typed quit
        print("Game ended.")
        break
    if player_choice not in choices: #continue the game if the user types sommething other than choices
        print("Invalid choice! Try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("Draw!")
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        print("Player wins!")
    else:
        print("Computer wins!")
