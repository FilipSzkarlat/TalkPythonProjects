while True:
    print('Zeby zakończyć wciśnij 0')
    number = input('podaj mi liczbę, a ja Ci powiem czy jest ona parzysta czy nie:')
    try:
        number = int(number)
        if number == 0:
            break
        if number % 2 == 1:
            print('To jest liczba NIEPARZYSTA')
        else:
            print('To jest liczba PARZYSTA')
    except ValueError:
        print('O nie nie, miała być LICZBA!')
    print('-------------------------------------------------------------------------------')

print('Bye bye')