import random

print('----------------------------')
print("        M&M's Game")
print('----------------------------')
print('Guess the number of M&Ms (1 to 100) and you get lunch on the house!')
start = 0
finish = 101
attempts = 0
our_num = []
last_guess = 0
for i in  range(100):
    our_num.append(i+1)

while True:
    print('---------------------------------------------------')

    print('żeby się poddać wciśnij 0')
    attempts += 1
    print(our_num)
    guess = input('How many M&Ms are in the jar?: ')
    if len(guess) == 0:
        continue
    try:
        guess = int(guess)

    except ValueError:
        print('a tu kod wygląda tak attemps += 2 ;)')
        attempts += 2
        continue

    if guess == 0:
        if last_guess <= start:
            print(f'Chodziło mi o {our_num[0]}')
            print(f'Gra zakończona po {attempts-1} rundach')
        else:
            print(f'Chodziło mi o {our_num[-1]}')
            print(f'Gra zakończona po {attempts-1} rundach')
        break

    if guess not in our_num:
        if guess <= start:
            print('That is too LOW')
        else:
            print('That is too HIGH')
        continue

    if len(our_num)==1:
        if guess == our_num[0]:
            print(f'Gratki, chodziło o {our_num[0]}')
            print(f'Udało Ci się zgadnąć za {attempts} próbą ;)')
            break
    x = int(len(our_num)/2)

    if guess <= our_num[x-1]:
        print('That is too LOW')
        for i in range(guess-start):
            our_num.pop(0)
        start = guess

    else:
        print('That is to HIGH')
        for i in range(finish-guess):
            our_num.pop()
        finish = guess
    last_guess = guess

