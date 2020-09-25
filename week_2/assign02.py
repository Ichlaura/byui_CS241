# Lewis Lockhart :: CS-241

def prompt_for_file_name():
    file_name = input("Please enter the data file: ")
    return file_name


def process_data():

    data_stash = {
        "highest_rate_data": [],
        "lowest_rate_data": [],
        "comm_rates": []
    }

    with open(prompt_for_file_name(), "r") as process_file:

        high_rate = -1
        low_rate = 1
        high_rate_data = []
        low_rate_data = []
        c_rates = []
        past_first_line = False

        for line in process_file:
            if past_first_line:
                line_list = line.split(",")
                current_rate = float(line_list[6])
                c_rates.append(float(current_rate))

                if current_rate > high_rate:
                    high_rate = current_rate
                    high_rate_data = line_list

                if current_rate < low_rate:
                    low_rate = current_rate
                    low_rate_data = line_list
            else:
                past_first_line = True

        data_stash["comm_rates"] = c_rates
        data_stash["highest_rate_data"] = high_rate_data
        data_stash["lowest_rate_data"] = low_rate_data

        return data_stash


def main():
    data = process_data()
    print(data)


if __name__ == "__main__":
    main()
