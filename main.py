from _skelet_functions import *
import itertools

COMBINATIONS = ['A', 'B', 'C', 'D', 'E', 'F']
MENU_OPTIONS = [
    'Typ het nummer in wat bij uw keuze hoort;',
    '1: Player vs Computer',
    '6: Beëindigen'
]


def game_loop():
    RANDOM_COMBINATION = create_random_combination()
    turn = 1
    while turn < 11:
        guess = []
        guess[:0] = request_valid_input(text='Uw combinatie: ', kind=0)

        feedback = feedback_calculate(['D', 'D', 'A', 'E'], guess)

        feedback_and_guess = 'z' * feedback[0] + 'o' * (4 - feedback[0]) + ' ' + ' - '.join(guess) + ' ' + 'w' * \
                             feedback[1] + 'o' * (4 - feedback[1])

        print(feedback_and_guess)

        if feedback[0] == 4:
            print('Je heb gewonnen!!')
            break

        turn += 1
        if turn > 10:
            print(f'Jammer je beurten zijn op, de juiste code was: {" - ".join(RANDOM_COMBINATION)}')

    menu()


def menu():
    for option in MENU_OPTIONS:
        print(option)

    menu_keuze = request_valid_input(text='Menu keuze: ', kind=1)

    if menu_keuze == 1:
        game_loop()
    if menu_keuze == 6:
        quit()


test = itertools.combinations_with_replacement(COMBINATIONS, 4)
# for i in test:
    # print(i)


menu()
