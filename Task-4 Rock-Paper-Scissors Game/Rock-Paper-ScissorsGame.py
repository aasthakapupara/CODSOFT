# CODSOFT/Python programming internship/Task 4/Rock-Paper-Scissors Game

import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'win'
    else:
        return 'lose'

def play_round():
    print("\nRock-Paper-Scissors Game")
    print("Choose: rock, paper, or scissors")
    
    user_choice = input("Your choice: ").lower()
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return
    
    computer_choice = get_computer_choice()
    print(f"Computer's choice: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    
    if result == 'win':
        print("Congratulations! You win!")
    elif result == 'lose':
        print("Sorry, you lose. Better luck next time!")
    else:
        print("It's a tie!")
    
    return result

def main():
    user_score = 0
    computer_score = 0

    while True:
        result = play_round()
        if result == 'win':
            user_score += 1
        elif result == 'lose':
            computer_score += 1
        
        print(f"\nScore - You: {user_score} | Computer: {computer_score}")
        
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    print("\nThanks for playing!")
    print(f"Final Score - You: {user_score} | Computer: {computer_score}")

if __name__ == "__main__":
    main()
