import random
import itertools

from _skelet_functions import *


def create_list_of_combinations(combinations, n):
    """

    Create a list of all the possible combinations

    :param combinations:
    :param n:
    :return:

    """
    all_possibilities = list(itertools.product(combinations, repeat=n))
    all_possibilities = [list(x) for x in all_possibilities]
    return all_possibilities


def simple_strategy(guesses, answer, possibilities=None):
    """

    Overview function that calls all functions for the simple strategy

    :param guesses:
    :param answer:
    :param possibilities:
    :return:

    """

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
    """

    Remove possibilities with written out rules

    :param guesses:
    :param possibilities:
    :return:

    """

    black_pawn_last_guess = guesses[-1]['A'][1]
    white_pawn_last_guess = guesses[-1]['A'][0]

    pawns = black_pawn_last_guess + white_pawn_last_guess

    last_guess = guesses[-1]['Q']
    remaining_possibilities = []

    '''
    
    Rule 1: 
    
    If feedback has no white and black pawns add the possible options to the new list.
    
    '''
    if black_pawn_last_guess == 0 and white_pawn_last_guess == 0:
        for reeks in possibilities:
            valid = True
            for letter in last_guess:
                if letter in reeks:
                    valid = False

            if valid:
                remaining_possibilities.append(reeks)

    '''
    
    Rule 2:
    
    If feedback has 4 white or the black and white add up to 4 pawns add the possible options to the new list
    
    '''

    if black_pawn_last_guess + white_pawn_last_guess == 4:
        for reeks in possibilities:
            valid = True
            for letter in last_guess:
                if letter not in reeks:
                    valid = False

            if valid:
                remaining_possibilities.append(reeks)


    '''
    
    Rule 3:
    
    If feedback has 1 or 2 or 3 white or black pawns add the possible options to the new list
    
    '''

    if pawns == 3 or pawns == 2 or pawns == 1:
        for reeks in possibilities:
            similarities = 0
            for letter in last_guess:
                if letter in reeks:
                    similarities += 1

            if similarities > pawns:
                remaining_possibilities.append(reeks)
    return remaining_possibilities
