# Lewis Lockhart :: CS-241
import re


def prompt_filename():
    # get file name from user
    f_name = input('Please enter a filename: ')
    return f_name


def prompt_word_search():
    # get word to search
    s_word = input("Please enter a word to count: ")
    return s_word


def parse_file(filename, search):
    # open the file
    file = open(filename, encoding="utf8")

    w_count = 0
    # loops through each line in the file
    for line in file:
        # splits before and after words on spaces and other chars
        words = re.split('\s|(?<!\d)[-,—().:!?+=;\"\'\“](?!\d)', line)
        # loops through each word in a line
        for word in words:
            # makes all words lowercase for comparison
            lower = word.lower()
            # compares current word with search word
            if lower == search:
                w_count += 1
    file.close()
    return w_count


def main():
    # holds filename
    filename = prompt_filename()
    # user feedback
    print(f'Opening file {filename}')
    # holds word to search
    search = prompt_word_search()
    # get word count from parse_file
    word_count = parse_file(filename, search)
    # user result feedback
    print(f"The word '{search}' occurs {word_count} times in this file.")


if __name__ == "__main__":
    main()
