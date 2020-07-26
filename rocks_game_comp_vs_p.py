import random


def main():
    header()
    play_game('Player', 'Computer')

def header():
    print('----------------------------')
    print('    Rock Paper Scissors')
    print('----------------------------')

def get_roll(player_name, rolls):
    roll = input(f'{player_name}, what is your roll? [rock, paper, scissors]: ')
    roll = roll.lower().strip()
    if roll not in rolls:
        print(f'Sorry {player_name}, {roll} is not a valid play!')
        return None
    return roll

def play_game(player_1, player_2):
    rounds = 3
    wins_p1 = 0
    wins_p2 = 0

    rolls = ['rock', 'paper', 'scissors']

    while wins_p1 < rounds and wins_p2 < rounds:

        roll = get_roll(player_1, rolls)
        roll2 = random.choice(rolls)

        if not roll:
            print("Can't play that, exiting")
            return

        print(f'{player_1} rolls {roll}')
        print(f'{player_2} rolls {roll2}')

        winner = check_for_winning_throw(player_1, player_2, roll, roll2)
        if winner is None:
            print('This round was a tie!')
        else:
            print(f'{winner} takes the round!')

    overall_winner = None
    if wins_p1 >= rounds:
        print(f'{player_1} wins the game!')
    else:
        print(f'{player_2} wins the game!')

        if winner == player_1:
            wins_p1 += 1
        else:
            print(f'{player_2} wins the game!')

def check_for_winning_throw(player_1, player_2, roll1, roll2):
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
    return winner


if __name__ == '__main__':
    main()
