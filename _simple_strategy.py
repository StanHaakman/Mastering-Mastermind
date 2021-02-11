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

    if len(guesses) < 1:
        remaining_answers = create_list_of_combinations(COMBINATIONS, 4)

        guess = remaining_answers[0]

        feedback = feedback_calculate(answer, guess)
    else:
        remaining_answers = remove_impossible_guesses(guesses, possibilities)

        guess = remaining_answers[0]

        feedback = feedback_calculate(answer, guess)

    return guess, feedback, remaining_answers


def remove_impossible_guesses(guesses, possibilities):
    """

    Remove possibilities with written out rules

    :param guesses:
    :param possibilities:
    :return:

    """

    last_guess = guesses[-1]['Q']
    feedback = guesses[-1]['A']

    remaining_possibilities = []

    for possible in possibilities:
        if feedback == feedback_calculate(last_guess, possible):
            if last_guess != possible:
                remaining_possibilities.append(possible)

    return remaining_possibilities
