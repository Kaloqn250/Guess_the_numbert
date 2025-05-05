import random

computer_number = random.randint(1, 100)

while True:
    player_data = input('Guess a number between 1 - 100: ')

    if not player_data.isdigit():
        print('Opps. Invalid data. Try again ...')
        continue

    player_number = int(player_data)

    if player_number == computer_number:
        print('That\'s it. You\'ve guessed it')
        break
    elif player_number > computer_number:
        print('A bit too high')
    else:
        print('A bit too low')