import random

COMBINATIONS = ['A', 'B', 'C', 'D', 'E', 'F']


def create_random_combination():
    """
    Create and return an random combination of 4
    """

    combination = []
    for i in range(4):
        combination.append(COMBINATIONS[random.randint(0, 5)])

    return combination


def ask_for_input(text):
    """
    Really easy request for input from the user
    """

    input_text = input(text).upper()
    return input_text


def validate(input_text, kind):
    """
    Function to check of the input from the user is valid.

    kind stands for which validation check have to be performed.

    - kind: 0 stands for the combination validation
        - If all the letters are possible answers
        - If the input_text is a string
        - If input_text contains exactly 4 characters
    - kind: 1 stands for the menu-item validation
        - If the input_text is an interger
        - If the input_text isn't higher than the highest menu-item
    """

    valid = True

    if kind == 0:
        for letter in input_text:
            if type(letter) != str or letter not in COMBINATIONS or len(input_text) != 4:
                valid = False
    elif kind == 1:
        try:
            input_text = int(input_text)
        except ValueError:
            valid = False

        if input_text > 6:
            valid = False

    return valid


def request_valid_input(text, kind):
    """
    This is the main input/validate function.
    It works as a sort of loop that keeps calling himself untill the validation is correct.

    At that point the function returns the user input_text to the main game loop
    """

    input_text = ask_for_input(text)

    if validate(input_text, kind):
        if kind == 1:
            return int(input_text)
        return input_text
    print('Invoer invalid. Probeer opnieuw')
    return request_valid_input(text, kind)


def feedback_calculate(answer, guess):
    """
    In this function I'm handeling the guess from the player or computer.

    I'm returning this value as described in the artikel, Yet another mastermind strategy.
    Its going to be a list with 2 items.
        - The first number refers to the ammount of 'pawns' that are in the right position and the right color.
          In this case the its a correct Letter and on the right index.
          If this is the case i change the value in the guess and answer copied list to 'Z' or 'W'

        - The second number refers to the ammount of 'pawns' that are just the right color.
          In this case the its a correct Letter.
    """

    tmp_answer = answer.copy()
    tmp_guess = guess.copy()

    feedback = [0, 0]

    for i, c in enumerate(tmp_guess):
        if c in tmp_answer and i == tmp_answer.index(c):
            tmp_answer[i] = 'Z'
            tmp_guess[i] = 'W'
            feedback[0] += 1

    for i, c in enumerate(tmp_guess):
        if c in tmp_answer:
            feedback[1] += 1

    return feedback

