from character import Enemy
import random

def get_user_choice():
    user_choice = input("Rock, Paper, or Scissors? ").strip().lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Invalid choice. Please choose Rock, Paper, or Scissors: ").strip().lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Alex wins!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"You chose {user_choice}")
    print(f"Alex chose {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!"  "If you lose, I will turn you into a burger")
    play_game()
