import random
emojis = {'r':'🪨','p':'📃','s':'✂️'}
choices = ('r','p','s')

while True:
    user_choice = input("rock paper or scissors: ? (r/p/s) ").lower()
    #if user_choice !='r' and user_choice != 'p' and user_choice != 's' :
    if user_choice not in choices:
        print("Invalid Choice")
        continue

    computer_choice = random.choice(choices)

    print(f'computer Chose {emojis[user_choice]}')
    print(f'computer Chose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print('Tie!')
    elif (
        (user_choice == 'r' and computer_choice == 's') or 
        (user_choice == 's' and computer_choice == 'p') or 
        (user_choice == 'p' and computer_choice == 'r')):
        print('You Win')
    else :
        print('You lose')
    should_contnue = input('You want to continue:?  (y/n) ').lower()
    if should_contnue == 'n':
        break