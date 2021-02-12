import random
import itertools

COMBINATIONS = ['A', 'B', 'C', 'D', 'E', 'F']


def create_random_combination():
    """

    Create and return an random combination of 4

    :return:

    """

    combination = []
    for i in range(4):
        combination.append(COMBINATIONS[random.randint(0, 5)])

    return combination


def ask_for_input(text):
    """

    Really easy request for input from the user

    :param text:
    :return:

    """

    input_text = input(text).upper()
    if input_text == '':
        ask_for_input(text)
    return input_text


def validate(input_text, validation_kind):
    """

    Function to check of the input from the user is valid.

    kind stands for which validation check have to be performed.

    - validation_kind: 0 stands for the combination validation
        - If all the letters are possible answers
        - If the input_text is a string
        - If input_text contains exactly 4 characters
    - validation_kind: 1 stands for the menu-item validation
        - If the input_text is an integer
        - If the input_text isn't higher than the highest menu-item
    - validation_kind: 2 stands for the amount of turn

    :param input_text:
    :param validation_kind:
    :return:

    """

    valid = True

    if validation_kind == 0 or validation_kind == 3:
        for letter in input_text:
            if type(letter) != str or letter not in COMBINATIONS or len(input_text) != 4:
                valid = False
    elif validation_kind == 1:
        try:
            input_text = int(input_text)
            if input_text > 6:
                valid = False
        except ValueError:
            valid = False
    elif validation_kind == 2:
        try:
            input_text = int(input_text)
        except ValueError:
            valid = False

    return valid


def request_valid_input(text, validation_kind):
    """

    This is the main input/validate function.
    It works as a sort of loop that keeps calling himself until the validation is correct.

    At that point the function returns the user input_text to the main game loop

    :param text:
    :param kind:
    :return:

    """

    input_text = ask_for_input(text)

    if validate(input_text, validation_kind):
        if validation_kind == 1 or validation_kind == 2:
            return int(input_text)
        elif validation_kind == 3:
            return list(input_text)
        return input_text
    print('Invoer invalid. Probeer opnieuw')
    return request_valid_input(text, validation_kind)


def feedback_calculate(answer, guess):
    """

    In this function I'm handling the guess from the player or computer.

    I'm returning this value as described in the article, Yet another mastermind strategy.
    Its going to be a list with 2 items.
        - The first number refers to the amount of 'pawns' that are in the right position and the right color.
          In this case the its a correct Letter and on the right index.
          If this is the case I change the value in the guess and answer copied list to 'Z' or 'W' for Zwart,
          Dutch for black because the 'B' was already in the combination, and White.

        - The second number refers to the amount of 'pawns' that are just the right color.
          In this case the its a correct Letter.

          If this is the case I change the value in the answers list to a 'T' for taken

    :param answer:
    :param guess:
    :return:

    """

    tmp_answer = answer.copy()
    tmp_guess = guess.copy()

    feedback = [0, 0]

    for i, c in enumerate(tmp_guess):
        if tmp_answer[i] == tmp_guess[i]:
            tmp_answer[i] = 'Z'
            tmp_guess[i] = 'W'
            feedback[0] += 1

    for i, c in enumerate(tmp_guess):

        if c in tmp_answer:
            tmp_answer[tmp_answer.index(c)] = 'T'
            feedback[1] += 1

    return feedback


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
