# A Randomized Password Generator

# Importing a Needed Module
import random
from random import choice, randint

# CONSTANTS
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    """A function that generates a random password"""
    rand_letters = [choice(LETTERS) for _ in range(randint(8, 10))]
    rand_numbers = [choice(NUMBERS) for _ in range(randint(2, 4))]
    rand_symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))]

    # Creating Needed Variables
    all_choices = [LETTERS, NUMBERS, SYMBOLS]
    sum_of_characters = len(rand_letters) + len(rand_numbers) + len(rand_symbols)
    password = ''

    # Shuffling the Previously Made Random Lists and Creating a Random Password
    # Without Using random.shuffle()
    while True:
        rn_choice = random.choice(all_choices)
        if rn_choice == LETTERS and len(rand_letters) != 0:
            password += rand_letters.pop(0)
        if rn_choice == NUMBERS and len(rand_numbers) != 0:
            password += rand_numbers.pop(0)
        if rn_choice == SYMBOLS and len(rand_symbols) != 0:
            password += rand_symbols.pop(0)
        if len(password) == sum_of_characters:
            break

    return password
