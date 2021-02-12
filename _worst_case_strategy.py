from _skelet_functions import *


def worst_case_strategy(guesses, answer, possibilities=None):
    if len(guesses) < 1:
        remaining_answers = create_list_of_combinations(COMBINATIONS, 4)

        guess = remaining_answers[7]

        feedback = feedback_calculate(answer, guess)
    else:
        remaining_answers = remove_impossible_guesses(guesses, possibilities)

        index = calc_worst_guess(guesses, remaining_answers)

        guess = remaining_answers[index]

        feedback = feedback_calculate(answer, guess)

    return guess, feedback, remaining_answers


def calc_worst_guess(guesses, possibilities):
    """

    loop through the remaining possibilities. Count the amount with the same feedback or better.
    return the index of the highest amount of occurences

    !!doesn't work yet!!

    :param guesses:
    :param possibilities:
    :return:
    """

    last_guess = guesses[-1]['Q']
    feedback = guesses[-1]['A']

    feedback_and_occurences = {}

    # Create list to count which options have the highest amount of possibilities
    for possible in possibilities:
        tmp_feedback = feedback_calculate(last_guess, possible)

        tmp_feedback = str(tmp_feedback)
        try:
            feedback_and_occurences[tmp_feedback] = feedback_and_occurences[tmp_feedback] + 1

        except KeyError:
            feedback_and_occurences[tmp_feedback] = 1

    worst_case_feedback = max(feedback_and_occurences, key=feedback_and_occurences.get)

    for i, possible in enumerate(possibilities):

        if worst_case_feedback == str(feedback_calculate(last_guess, possible)):
            print(i)
            return i
    return 0


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
