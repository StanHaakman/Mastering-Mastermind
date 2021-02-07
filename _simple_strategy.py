import random
import itertools

from _skelet_functions import *


def create_list_of_combinations(combinations, n):
    all_possibilities = list(itertools.product(combinations, repeat=n))
    all_possibilities = [list(x) for x in all_possibilities]
    return all_possibilities


def simple_strategy(guesses, answer, possibilities=None):
    if possibilities is None:
        possibilities = []
    if len(guesses) < 1:
        possibilities = create_list_of_combinations(COMBINATIONS, 4)

        guess = possibilities[random.randint(0, len(possibilities) - 1)]

        feedback = feedback_calculate(answer, guess)
    else:
        possibilities = remove_impossible_guesses(guesses, possibilities)

        guess = possibilities[random.randint(0, len(possibilities) - 1)]

        feedback = feedback_calculate(answer, guess)

    remaining_answers = possibilities
    return guess, feedback, remaining_answers


def remove_impossible_guesses(guesses, possibilities):

    black_pawn_last_guess = guesses[-1]['A'][1]
    white_pawn_last_guess = guesses[-1]['A'][0]

    last_guess = guesses[-1]['Q']

    '''
    
    Rule 1: 
    
    If feedback has no white and black pawns remove all possibilities with those characters.
    
    '''
    if black_pawn_last_guess == 0 and white_pawn_last_guess == 0:
        for reeks in possibilities:
            valid = True
            for getal in last_guess:
                if getal in reeks:
                    valid = False

            if not valid:
                possibilities.remove(reeks)
        print('0 Goede')

    '''
    
    Rule 2:
    
    If feedback has 4 white or the black and white add up to 4 pawns remove all possibilities without all these 4 
    
    '''

    if black_pawn_last_guess + white_pawn_last_guess == 4:
        print(last_guess)
        for reeks in possibilities:
            valid = True
            for getal in last_guess:
                if getal not in reeks:
                    valid = False

            if not valid:
                possibilities.remove(reeks)
                print(reeks)
                print('Remove')
            else:
                print(reeks)
                print('keep')
        print('4 Goede')

    return possibilities
