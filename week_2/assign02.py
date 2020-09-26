# Lewis Lockhart :: CS-241

# prompts for and returns file name entered by user
def prompt_for_file_name():
    file_name = input("Please enter the data file: ")
    print('')
    return file_name


def process_data():
    # holds values to be returned
    data_stash = {
        "highest_rate_data": [],
        "lowest_rate_data": [],
        "comm_rates": []
    }
    # opens file and parses data into data_stash
    with open(prompt_for_file_name(), "r") as process_file:
        # var list
        high_rate = -1
        low_rate = 1
        high_rate_data = []
        low_rate_data = []
        c_rates = []
        past_first_line = False

        # loops through lines in the file
        for line in process_file:
            if past_first_line:
                line_list = line.split(",")
                current_rate = float(line_list[6])
                c_rates.append(float(current_rate))
                # updates the high_rate and high_rate_data
                if current_rate > high_rate:
                    high_rate = current_rate
                    high_rate_data = line_list
                # updates the low_rate and the low_rate_data
                if current_rate < low_rate:
                    low_rate = current_rate
                    low_rate_data = line_list
            else:
                past_first_line = True

        # loads the data_stash
        data_stash["highest_rate_data"] = high_rate_data
        data_stash["lowest_rate_data"] = low_rate_data
        data_stash["comm_rates"] = c_rates

        return data_stash


def output_average(rate_list):
    # var list
    rate_count = 0
    rate_total = 0.0

    # increments rate_count and rate_total
    for r in rate_list:
        rate_count += 1
        rate_total += r

    # calculates average rate
    average_rate = rate_total / rate_count

    # outputs information to the user
    print(f'The average commercial rate is: {average_rate}')
    print('')


def output_high(h_rate):
    print('The highest rate is:')
    # parses information into the required format
    print(f'{h_rate[2]} ({h_rate[0]}, {h_rate[3]}) - ${float(h_rate[6])}')
    print('')


def output_low(l_rate):
    print('The lowest rate is:')
    # parses information into the required format
    print(f'{l_rate[2]} ({l_rate[0]}, {l_rate[3]}) - ${float(l_rate[6])}')


def main():
    data = process_data()
    output_average(data['comm_rates'])
    output_high(data["highest_rate_data"])
    output_low(data["lowest_rate_data"])


if __name__ == "__main__":
    main()
