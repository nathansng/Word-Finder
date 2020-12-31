"""
Word_Finder is a program that takes in a collection of letters and returns
all possible words that can be created from those letters. There is also a
Scrabble option where the program will sort the possible words by the highest
points possible from the words.
"""

# Import modules for reading dataframe
import pandas as pd

english_words = pd.read_csv("english_words_letter_count.csv")

def find_words(letters):
    """
    Returns a list of all possible words given a list of letters

    Parameter
        letters - list or string, List/String of letters
    Return
        list - List of all words
    """
    # Create a count dict of letters given
    alpha = "abcdefghijklmnopqrstuvwxyz"
    chars = {}
    for char in alpha:
        chars[char] = 0

    for letter in letters:
        chars[letter.lower()] += 1

    possible_words = english_words.copy()

    for char in alpha:
        possible_words = possible_words.loc[possible_words[char] <= \
            chars[char]]

    return list(possible_words["Word"])


# Scrabble Points per Letter
letter_points = pd.read_csv("Scrabble_Letter_Points.csv")


def points(word):
    """
    Returns the number of points based on the letters in the word

    Parameter
        word - string, Word to calculate points from
    Return
        int - Number of points
    """
    score = 0
    for letter in word.lower():
        letter_score = letter_points.loc[letter_points["Letter"]==letter]
        score += letter_score["Points"].values[0]
    return score

def scrabble_points(letters):
    """
    Returns a sorted dictionary of the highest scoring words possible,
    according to scrabble rules.

    Parameter
        letters - list or string, List/String of letters
    Return
        dict - dictionary of possible words and associated points
    """
    possible_words = find_words(letters)

    word_points = {}
    for word in possible_words:
        word_points[word] = points(word)

    # Sort dictionary by highest points
    word_points = sorted(word_points.items(), key = lambda key_value: \
        (key_value[1], key_value[0]), reverse=True)

    return dict(word_points)




