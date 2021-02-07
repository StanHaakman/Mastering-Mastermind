from _simple_strategy import simple_strategy, create_list_of_combinations
from _skelet_functions import *

COMBINATIONS = ['A', 'B', 'C', 'D', 'E', 'F']
MENU_OPTIONS = [
    'Typ het nummer in wat bij uw keuze hoort;',
    '1: Player vs Computer',
    '2: Computer vs Computer, Simple strategy',
    '6: Beëindigen'
]

GUESSES = []


def store_data(guess, feedback):
    GUESSES.append({'Q': guess, 'A': feedback})


def game_loop(kind):
    RANDOM_COMBINATION = create_random_combination()
    print(f'Right answer: {RANDOM_COMBINATION}')
    turn = 1
    possibilities = None
    while turn < 11:

        if kind == 0:

            guess = []
            guess[:0] = request_valid_input(text='Uw combinatie: ', kind=0)

            feedback = feedback_calculate(RANDOM_COMBINATION, guess)

            feedback_and_guess = 'z' * feedback[0] + 'o' * (4 - feedback[0]) + ' ' + ' - '.join(guess) + ' ' + 'w' * \
                                 feedback[1] + 'o' * (4 - feedback[1])

            print(feedback_and_guess)

        elif kind == 1:

            guess, feedback, possibilities = simple_strategy(GUESSES, RANDOM_COMBINATION, possibilities=possibilities)

        store_data(guess, feedback)

        if feedback[0] == 4:
            print('Je heb gewonnen!!')
            break

        turn += 1
        if turn > 10:
            print(f'Jammer je beurten zijn op, de juiste code was: {" - ".join(RANDOM_COMBINATION)}')
            GUESSES.clear()
    menu()


def menu():
    for option in MENU_OPTIONS:
        print(option)

    menu_keuze = request_valid_input(text='Menu keuze: ', kind=1)

    if menu_keuze == 1:
        # Player vs Computer
        game_loop(kind=0)
    elif menu_keuze == 2:
        # Computer vs Computer, 'Simple strategy'
        game_loop(kind=1)
    elif menu_keuze == 6:
        quit()


menu()
