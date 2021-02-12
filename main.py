from _simple_strategy import simple_strategy
from _worst_case_strategy import worst_case_strategy

from _skelet_functions import *

COMBINATIONS = ['A', 'B', 'C', 'D', 'E', 'F']
MENU_OPTIONS = [
    'Typ het nummer in wat bij uw keuze hoort;',
    '1: Player vs Computer',
    '2: Computer vs Computer, Simple strategy',
    '3: Computer vs Computer, Simple strategy. Set own amount.',
    '4: Computer vs Player',
    '5: Computer vs Computer, Worst case. set own amount. Not working!',
    '6: Beëindigen'
]

GUESSES = []


def store_data(guess, feedback):
    GUESSES.append({'Q': guess, 'A': feedback})


def game_loop(kind):
    """

    Call different functions based on the chosen game in the menu

    kind:
    - 0 Player vs Computer
    - 1 Computer vs Computer, Simple strategy
    - 2 Computer vs Computer, Simple strategy. Set own amount.
    - 3 Computer vs Player

    :param kind:
    :return:
    """

    possibilities = None
    if kind == 2 or kind == 4:
        amount_of_games = request_valid_input(text='Aantal spellen: ', validation_kind=2)
        turns = []

        for i in range(amount_of_games):
            turn = 1
            RANDOM_COMBINATION = create_random_combination()
            while True:

                if kind == 2:
                    guess, feedback, possibilities = simple_strategy(GUESSES, RANDOM_COMBINATION,
                                                                     possibilities=possibilities)
                elif kind == 4:
                    guess, feedback, possibilities = worst_case_strategy(GUESSES, RANDOM_COMBINATION,
                                                                         possibilities=possibilities)

                # Save guess and feedback to the to a guesses dictionary
                store_data(guess, feedback)

                # If the feedback contains 4 black pawns the game is over
                if feedback[0] == 4:
                    RANDOM_COMBINATION.clear()
                    possibilities.clear()
                    GUESSES.clear()
                    turns.append(turn)
                    break

                turn += 1

        gem_turn = sum(turns) / len(turns)
        print(f'Het gemiddelde over de {amount_of_games} pogingen was {gem_turn}')

    else:
        turn = 1

        if kind == 3 or kind == 0:
            RANDOM_COMBINATION = request_valid_input(text='Geheime combinatie: ', validation_kind=3)
        else:
            RANDOM_COMBINATION = create_random_combination()

        while True:

            if kind == 0:

                guess = []
                guess[:0] = request_valid_input(text='Uw combinatie: ', validation_kind=0)

                feedback = feedback_calculate(RANDOM_COMBINATION, guess)

                feedback_and_guess = 'z' * feedback[0] + 'o' * (4 - feedback[0]) + ' ' + ' - '.join(guess) + ' ' + 'w' * \
                                     feedback[1] + 'o' * (4 - feedback[1])

                print(feedback_and_guess)

            else:

                guess, feedback, possibilities = simple_strategy(GUESSES, RANDOM_COMBINATION,
                                                                 possibilities=possibilities)

            # Save guess and feedback to the to a guesses dictionary
            store_data(guess, feedback)

            # If the feedback contains 4 black pawns the game is over
            if feedback[0] == 4:
                print(f'Je heb gewonnen!!\nIn {turn} pogingen')
                RANDOM_COMBINATION.clear()
                if kind != 0:
                    possibilities.clear()
                GUESSES.clear()
                break

            turn += 1

            # If the current player runs out of turns return the program to the main menu
            if turn > 10:
                print(f'Jammer je beurten zijn op, de juiste code was: {" - ".join(RANDOM_COMBINATION)}')
                RANDOM_COMBINATION.clear()
                possibilities = None
                GUESSES.clear()
                break


def menu():
    """

    This is the function that shows the menu when code is run

    :return:
    """
    for option in MENU_OPTIONS:
        print(option)

    menu_keuze = request_valid_input(text='Menu keuze: ', validation_kind=1)

    if menu_keuze == 1:
        # Player vs Computer
        game_loop(kind=0)
    elif menu_keuze == 2:
        # Computer vs Computer, 'Simple strategy'
        game_loop(kind=1)
    elif menu_keuze == 3:
        # Computer vs Computer, 'Simple strategy' but with the choice of the amount of games and
        # result with the average of turns
        game_loop(kind=2)
    elif menu_keuze == 4:
        # Computer vs player
        game_loop(kind=3)
    elif menu_keuze == 5:
        # Worst case
        game_loop(kind=4)
    elif menu_keuze == 6:
        quit()


while True:
    menu()
