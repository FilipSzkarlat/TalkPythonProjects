import random

print('----------------------------')
print("        M&M's Game")
print('----------------------------')
print('Guess the number of M&Ms and you get lunch on the house!')

mm_count = random.randint(1, 100)
attempt_limit = 5
attempts = 0

while True:
    guess = input('How many M&Ms are in the jar?: ')
    if len(guess) == 0:
        continue
    try:
        guess = int(guess)

    except ValueError:
        print('Z debilami nie gramy!!!')
        break
    attempts += 1
    if attempts == 5:
        print(f'Sorry, it was {mm_count}')
        print('Bye bye')
        break
    if mm_count == guess:
        print(f'You got a free lunch!!! It was {guess}.')
        print(f'You are done in {attempts} rounds!')
        break
    elif guess < mm_count:
        print('That is too LOW')
    else:
        print('That is to HIGH')
    print('---------------------------------------------------')


