"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car has set odometer correctly"

    test_car = Car(fuel=10)
    assert test_car.fuel == 10

    test_car = Car()
    assert test_car.fuel == 0


def format_phrase_to_sentence(phrase):
    """Format a phrase as a sentence, starting with capital and ending with .
    >>> format_phrase_to_sentence('hello')
    'Hello.'
    >>> format_phrase_to_sentence('i went to the shops.')
    'I went to the shops.'
    >>> format_phrase_to_sentence('I am going to the beach')
    'I am going to the beach.'
    """

    sentence = phrase.capitalize()
    if sentence[-1] != ".":
        sentence += '.'
    return sentence


run_tests()
doctest.testmod()
