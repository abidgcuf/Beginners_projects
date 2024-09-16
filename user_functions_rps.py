import random

emojis = {'r':'🪨','p':'📃','s':'✂️'}
choices = ('r','p','s')

def get_user_choice():
  while True:
    user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
    if user_choice in choices:
      return user_choice      
    else:
      print('Invalid choice!')

def display_choices(user_choice,computer_choice):
    print(f'computer Chose {emojis[user_choice]}')
    print(f'computer Chose {emojis[computer_choice]}')

def detrmine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif (
        (user_choice == 'r' and computer_choice == 's') or 
        (user_choice == 's' and computer_choice == 'p') or 
        (user_choice == 'p' and computer_choice == 'r')):
        print('You Win')
    else :
        print('You lose')

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)
        display_choices(user_choice,computer_choice)
        detrmine_winner(user_choice,computer_choice)
        should_contnue = input('You want to continue:?  (y/n) ').lower()
        if should_contnue == 'n':
            break    
play_game()       