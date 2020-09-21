# Lewis Lockhart :: CS-241

def get_file_name():
    # gets the file name from the user
    file_name = input("Enter file: ")
    return file_name


def process_file_data():
    # opens the file in read mode
    file = open(get_file_name(), "r")
    # result vars
    line_count = 0
    word_count = 0

    # loops over lines and words and updates the counts
    for line in file:
        line_count += 1
        num_words = line.split(" ")
        word_count += len(num_words)

    file.close()

    # creates return list
    results = [line_count, word_count]

    return results


def output_data(results_data):
    # prints the results to the console
    print(f"The file contains {results_data[0]} lines and {results_data[1]} words.")


def main():
    output_data(process_file_data())


if __name__ == "__main__":
    main()
