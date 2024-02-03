"""
This module takes in words separated by a character by the user, splits them into a list,
appends a default probability and saves the lists as a csv ordered dictionary file with
given headers.
"""

import csv
import os
import logging


def input_words_processing(words):
    """ list
    Converts input words to list, removes whitespaces and appends the Default probability
    """
    words_line_list = words.split('=')

    for word in words_line_list:
        word_fixed = word.strip()
        words_line_list[words_line_list.index(word)] = word_fixed

    words_line_list.append(0)  # Starting Probability_modifier
    return words_line_list


if not os.path.exists('data_words.csv'):
    # Creates data_words.csv if it doesn't exist and adds headers
    with open('data_words.csv', 'a', newline='') as append_file:
        writer = csv.writer(append_file)
        writer.writerow(['French', 'English', 'Probability_modifier'])

with open('data_words.csv', 'a', newline='') as append_file:
    # Appends lists (['French', 'English', 'Probability']) of words with the Default propability to data_words.csv.
    writer = csv.writer(append_file)
    print('\nTo insert words write them below and press Enter (format: -French word- = -Englis word-).'
          '\nWhen done with adding words press Enter as the last input.')

    while True:
        words_input = input('\033[0mInsert the Words: ')
        if words_input == '':
            print('\n\n')
            break

        elif '=' in words_input:
            words_list = input_words_processing(words_input)
            writer.writerow(words_list)
            print('\tWords added!')
            print('2')
        else:
            print("\033[0;31mYou have tp enter a French word and then an English word\n"
                  "separated by '='.")
