"""
This program first saves the user entered english and French words
in a CSV. After it calculates the probability of set of each word
to be picked and tests the user on that set. Last it checks the users
answer and changes the sets probability accordingly
"""
import logging
import csv
import input as my_input

with open('data_words.csv', 'r') as read_file:
    fieldnames = ['French', 'English', 'Probability_modifier']
    reader = csv.DictReader(read_file, fieldnames=fieldnames)
    reader = list(reader)  # convert iterator to iterable(list)

    try:
        probability_common = 1 / len(reader[1:])
    except ZeroDivisionError:
        logging.fatal('You have to enter attlist one set of words.\n'
                      '\t\tPress enter to exit.')
        input()
        quit()
    print('Words test:\n'
          '\tWrite the following words in french.\n')

    import data_handling as dh
    while True:
        # While user is entering answers.
        # Gets random line from reader and tests user on word.
        # Then changes probability accordingly
        rand_line = dh.get_rand_line(reader, probability_common)
        user_word = input(f'\033[0m\t{rand_line["English"]} = ')
        if user_word != '':
            dh.chk_user(user_word, rand_line, reader, fieldnames)
        else:
            break
