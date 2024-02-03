import csv
import random
from unidecode import unidecode


def chk_word(user_word, reference_word):
    """returns bool
    Compares the user entered word with the reference ignoring special characters.
    """
    check = unidecode(user_word.strip()) == unidecode(reference_word.strip())
    return check


def chk_user(user_word, rand_line, reader, fieldnames):
    """No return
    After checking the correctness of the user entered word,
    sends the appropriate message and changes the probability.
    """
    check = chk_word(user_word, rand_line['French'])

    learning_rate = 0.5  # Amount by how much the probability changes.
    if check:
        print(f'\033[1;32m\tCorrect (Right spelling: {rand_line["French"]})\n')
        rand_line['Probability_modifier'] = \
            float(rand_line['Probability_modifier']) - learning_rate
    else:
        print(f'\033[0;31m\tIncorrect. Right spelling: {rand_line["French"]}\n')
        rand_line['Probability_modifier'] = \
            float(rand_line['Probability_modifier']) + learning_rate

    with open('data_words.csv', 'w', newline='') as write_file:
        writer = csv.DictWriter(write_file, fieldnames=fieldnames)
        for line in reader:
            writer.writerow(line)


def get_rand_line(reader, probability_common):
    """returns list
    Calculates the probability of each word
    and chooses a random (weighted) line from reader
    """
    probability_list = []
    for line in reader[1:]:
        # Calculates the probability of each word and appends it to the probability_list.
        probability_modifier = float(line['Probability_modifier'])
        probability = probability_common + probability_modifier

        if probability < 0.1:
            probability = 0.1  # Probability must be > 0

        probability_list.append(probability)
    rand_line_index = random.choices(range(1, len(reader)), weights=probability_list)
    rand_line_index = rand_line_index[0]  # Convert list to dictionary
    rand_line = reader[rand_line_index]

    return rand_line
