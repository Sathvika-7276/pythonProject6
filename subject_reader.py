"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    read_data = read_file()
    process_data = get_data(read_data)
    print(process_data)
    print_newlines(process_data)


def read_file():
    input_file = open(FILENAME)
    data = input_file.readlines()
    input_file.close()
    return data


def get_data(read_data):
    nested_line = []
    for line in read_data:
        lines = line.strip()
        parts = lines.split(',')
        parts[2] = int(parts[2])
        nested_line.append(parts)
    return nested_line


def print_newlines(nested_line):
    for line in nested_line:
        print("{} is taught by {:12} and has {:3} students".format(*line))


main()
