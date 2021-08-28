"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    "Read data and display with formatting."
    data = get_data()
    display_subject_details(data)


def get_data():
    """Read data from text file."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        data.append(parts)

    input_file.close()
    return data


def display_subject_details(data):
    "Display formatted data."
    for piece_of_data in data:
        print("{} is taught by {:12} and has {} students".format(*piece_of_data))


main()
