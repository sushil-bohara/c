import random

def play_rock_paper_scissors():
    # Step 2: Define choices
    choices = ["Rock", "Paper", "Scissors"]
    
    while True:
        # Step 3: Input player choice
        player_choice = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()
        if player_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
        
        # Step 3: Generate computer choice
        computer_choice = random.choice(choices)
        
        # Step 5: Determine the winner
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Scissors" and computer_choice == "Paper") or \
             (player_choice == "Paper" and computer_choice == "Rock"):
            print("You win!")
        else:
            print("You lose!")
        
        # Step 7: Repeat or exit
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Start the game
play_rock_paper_scissors()
