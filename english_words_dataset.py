# Credit to dwyl for the json file of English words
# Link to Dataset: https://github.com/dwyl/english-words

"""
This file converts the json dictionary into a dataset of each English word
and the number of letters each word contains. This dataset will be used to
find words given any combination of letters.
"""

import json
import pandas as pd
import collections


# Convert the json file into a python dict
with open("english_words.json") as json_file:
    data = json.load(json_file)

# Make a dataframe containing all words in the dictionary
english_words = pd.DataFrame({"Word": list(data.keys())})


def num_chars(word, char):
    """
    Returns a dictionary containing the number of characters that appears
    in a word.

    Parameter
        word - str, Word to look through
        char - str, Character to look for
    Return
        int - Number of times char appears in word
    """
    count = 0
    for c in word:
        if c == char:
            count += 1
    return count

# For each letter, add a column corresponding to the number of times that
# letter appears in the word
letters = "abcdefghijklmnopqrstuvwxyz"
for letter in letters:
    english_words[letter] = english_words["Word"].apply(num_chars, \
        args = (letter))

# Convert dataframe to csv file
english_words.to_csv("english_words_letter_count.csv", index=False)