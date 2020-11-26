# Author: Gaurang Ruparelia
# Assignment #2 - TextAnalyzer
# Date due: 2020-10-09
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

####### DO NOT EDIT FUNCTIONS BELOW ########



def character_is_digit(char):
    """Indicates whether the value referenced by char parameter
    is a digit character

    :param char: character to check
    :return: True when char is a digit character, False otherwise

    >>> test_char = 'b'
    >>> character_is_digit(test_char)
    False
    >>> test_char = '2'
    >>> character_is_digit(test_char)
    True
    """

    return char.isdigit()


def character_is_letter(char):
    """Indicates whether the value referenced by char parameter
    is a letter

    :param char: character to check
    :return: True when char is a letter, False otherwise

    >>> test_char = 'b'
    >>> character_is_letter(test_char)
    True
    >>> test_char = '2'
    >>> character_is_letter(test_char)
    False
    """

    return char.isalpha()

####### DO NOT EDIT FUNCTIONS ABOVE ########


def main():
    """Runs a program for analyzing character counts from
    input text
    """

    # call run_text_analyzer() here and remove pass below
    run_text_analyzer()


def analyze_text():
    """Calls the functions to compute the number of total characters,
    spaces, digits, letters, and sentences in user-supplied text and to
    output the final counts when text input by user.

    :return: True when text provided, False when no text provided
    """

    user_text_input = input("Please enter text to analyze (press ENTER/return without text to exit): ")

    text_exists = True

    if user_text_input == "":
        text_exists = False
        return text_exists


    else:
        num_chars = total_character_count(user_text_input)
        num_spaces = character_is_whitespace(user_text_input)
        num_digits = character_digits(user_text_input)
        num_letters = character_letters(user_text_input)
        num_sentences = character_ends_sentence(user_text_input)

        print_results(num_chars, num_spaces, num_digits, num_letters, num_sentences)
        return text_exists



def run_text_analyzer():
    """Runs the Text Analyzer as a repeated sequence of
    prompting the user for input text and outputting the
    character counts computed from the input

    :return: None
    """
    print("Welcome to the Text Analyzer!")
    print()
    text_exists = True

    while text_exists == True:
        text_exists = analyze_text()

    print()
    print("Goodbye.")


def print_results(num_chars, num_spaces, num_digits, num_letters, num_sentences):
    """Prints the number of total characters, spaces, digits, letters,
    and sentences identified in the text being analyzed.

    :param num_chars: number of total characters in text
    :param num_spaces: number of spaces in text
    :param num_digits: number of digits in text
    :param num_letters: number of letters in text
    :param num_sentences: number of sentences in text
    :return: None

    # >>> num_chars = 234
    # >>> num_spaces = 14
    # >>> num_digits = 16
    # >>> num_letters = 201
    # >>> num_sentences = 21
    # >>> print_results(num_chars, num_spaces, num_digits, num_letters, num_sentences)"""

    print()
    print("Count of characters:", num_chars)
    print("Count of spaces:", num_spaces)
    print("Count of digits:", num_digits)
    print("Count of letters:", num_letters)
    print("Count of sentences:", num_sentences)
    print()

def total_character_count(user_text_input):
    """
    I spoke to Professor Reeves about this implementation as opposed to the docstring implementation, and he said it's okay

    Counts the total number of characters in the user's input text

    :param user_text_input: text provided by the user
    :return: the total character count in the string input
    """

    char_count = 0
    for char in user_text_input:
        char_count = char_count + 1

    return char_count

def character_letters(user_text_input):
    """
    I spoke to Professor Reeves about this implementation as opposed to the docstring implementation, and he said it's okay

    Counts the total number of alphabets/letters in the user's input text

    :param user_text_input: text provided by the user
    :return: the total alphabet count in the string input



    """

    letter_character_count = 0
    letter_options = 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for char in user_text_input:
        if char in letter_options:
            letter_character_count = letter_character_count + 1

    return letter_character_count

def character_digits(user_text_input):
    """
    I spoke to Professor Reeves about this implementation as opposed to the docstring implementation, and he said it's okay

    Counts the total number of digits in the user's input text

    :param user_text_input: text provided by the user
    :return: the total digit count in the string input

    """

    digit_character_count = 0
    digit_options = '0123456789'
    for char in user_text_input:
        if char in digit_options:
            digit_character_count = digit_character_count + 1

    return digit_character_count



def character_ends_sentence(user_text_input):
    """
    I spoke to Professor Reeves about this implementation as opposed to the docstring implementation, and he said it's okay

    Counts the total number of end of sentence characters in the user's input text
    :param user_text_input: text provided by the user
    :return: the total end of sentence character count



    eos is an acronym for end of sentence
    """

    eos_character_count = 0
    eos_options = ".?!"
    for char in user_text_input:
        if char in eos_options:
            eos_character_count = eos_character_count + 1

    return eos_character_count


def character_is_whitespace(user_text_input):
    """
    I spoke to Professor Reeves about this implementation as opposed to the docstring implementation, and he said it's okay

    Counts the total number of whitespace characters in the user's input text
    :param user_text_input: text provided by the user
    :return: the total whitespace character count
    """

    whitespace_character_count = 0
    whitespace_options = " \n \t"
    for char in user_text_input:
        if char in whitespace_options:
            whitespace_character_count = whitespace_character_count + 1

    return whitespace_character_count




    #<BLANKLINE>







# The total number of characters in the text. This is the total length of the text that is input into the program.
# The number of whitespace characters in the text. This is the total number of space characters (' '), tab characters ('\t'), and newline ('\n') characters in the input text.
# The number of digits in the input text. This value represents the count of characters that are 0, 1, 2, 3, 4, 5, 6, 7, 8, or 9. Take note that this is not the count of
# numbers in the text. So, if the text includes the number 123, this counts as 3 digits even though it represents 1 number.
# The number of alphabetic characters in the input text. This value represents the count of characters that are letters. The characters can be either uppercase or lowercase letters.
# The number of sentences in the input text. This value represents the count of sentences contained in the input. Counting sentences is actually a complicated task. To simplify this
# calculation, we will assume that a sentence exists wherever one of 3 characters is encountered in the input: a period ('.'), a question mark ('?'), or an exclamation point ('!').
# The analyze_text() function must return a bool value. When the user enters text, the function returns True. When the user presses Enter/return without typing any text, the function returns False.

    # >>> test_char = ' '
    # >>> character_is_whitespace(test_char)
    # True
    # >>> test_char = '#'
    # >>> character_is_whitespace(test_char)
    # False
    # >>> test_char = '\n'
    # >>> character_is_whitespace(test_char)
    # True
    # >>> test_char = '\t'
    # >>> character_is_whitespace(test_char)
    # True
    # """












    # >>> test_char = 'k'
    # >>> character_ends_sentence(test_char)
    # False
    # >>> test_char = '.'
    # >>> character_ends_sentence(test_char)
    # True
    # >>> test_char = '?'
    # >>> character_ends_sentence(test_char)
    # True
    # >>> test_char = '!'
    # >>> character_ends_sentence(test_char)
    # True
    # """


####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == '__main__':
    # Remove comments for next 4 lines to run doctests
    # print("Running doctests...")
    # import doctest
    # doctest.testmod(verbose=True)

    # print("\nRunning program...\n")

    main()
