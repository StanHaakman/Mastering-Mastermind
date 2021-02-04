from _skelet_functions import *

RANDOM_COMBINATION = create_random_combination()
MENU_OPTIONS = [
    'Typ het nummer in wat bij uw keuze hoort;',
    '1: Player vs Computer',
    '6: Beëindigen'
]


def game_loop():
    turn = 1
    while turn < 11:
        guess = []
        guess[:0] = request_valid_input(text='Uw combinatie: ', kind=0)

        feedback = feedback_calculate(RANDOM_COMBINATION, guess)

        print('x' * feedback[0] + 'o' * (4 - feedback[0]), ' - '.join(guess), 'x' * feedback[1] + 'o' * (4 - feedback[1]))

        if feedback[0] == 4:
            print('Je heb gewonnen!!')
            break

        turn += 1

    menu()


def menu():
    for option in MENU_OPTIONS:
        print(option)

    menu_keuze = request_valid_input(text='Menu keuze: ', kind=1)

    if menu_keuze == 1:
        game_loop()
    if menu_keuze == 6:
        quit()


menu()
