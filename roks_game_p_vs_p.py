print('----------------------------')
print('    Rock Paper Scissors')
print('----------------------------')

player_1 = input('Enter player 1 name: ')
player_2 = input('Enter player 2 name: ')

rolls = ['rock', 'paper', 'scissors']

roll1 = input(f'{player_1}, what is your roll? [rock, paper, scissors]: ')
roll1 = roll1.lower().strip()

if roll1 not in rolls:
    print(f'Sorry {player_1}, {roll1} is not a valid play!')

roll2 = input(f'{player_2}, what is your roll? [rock, paper, scissors]: ')
roll2 = roll2.lower().strip()
if roll2 not in rolls:
    print(f'Sorry {player_2}, {roll2} is not a valid play!')

print(f'{player_1} rolls {roll1}')
print(f'{player_2} rolls {roll2}')

winner = None

if roll1 == roll2:
    print('The play was tied!')

elif roll1 == 'rock':
    if roll2 == 'paper':
        winner = player_2
    else:
        winner = player_1

elif roll1 == 'paper':
    if roll2 == 'scissors':
        winner = player_2
    else:
        winner = player_1

elif roll1 == 'scissors':
    if roll2 == 'rock':
        winner = player_2
    else:
        winner = player_1
if winner != None:
    print(f'{winner} win the game!')