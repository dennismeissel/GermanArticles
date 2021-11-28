import os
import sys


def read_lines(filename):
    with open(filename, encoding="utf8") as file:
        return file.readlines()



def check_line(_line):
    _line = _line.strip('\n')
    if _line.endswith('MAS') or _line.endswith('FEM') or _line.endswith('NEU'):
        entries = _line.split('\t')
        if entries[0] != entries[1]:
            # It is not a main form of a word
            return None
        word_info = entries[2].split(':')
        if word_info[0] != 'SUB':
            # not a noun
            return None
        if word_info[1] != 'NOM':
            # Not 'Nominativ'
            return None
        if word_info[2] != 'SIN':
            # Not singular
            return None
        if word_info[3] == 'MAS':
            return 1, entries[0]
        if word_info[3] == 'FEM':
            return 2, entries[0]
        if word_info[3] == 'NEU':
            return 3, entries[0]
    return None


path_input = input("Enter the path to the words.dump file\n")
path_output = input("Enter the path to the output file\n")

path_input = path_input.strip('"')
path_output = path_output.strip('"')
lines = read_lines(path_input)

with open(path_output, mode='w', encoding="utf8") as file:
    for line in lines:
        result = check_line(line)
        if result is not None:
            file.write(result[1] + ";" + str(result[0]) + "\n")

