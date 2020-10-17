# Lewis Lockhart :: CS-241

def prompt_for_file_name():
    file_name = input("Please enter the data file: ")
    print('')
    return file_name


def process_data():
    with open(prompt_for_file_name(), "r") as file_to_process:

        for line in file_to_process:
            alt_line = line.replace(" ", "")
            return alt_line


def prove_stack():
    stack = process_data()
    open_stack = []

    for i in stack:
        if i in {"{", "(", "["}:
            open_stack.append(i)
        elif i in {"}", ")", "]"}:
            if len(open_stack) == 0:
                return "Not balanced"
            last_in = open_stack.pop()
            if last_in == "{" and i == "}" \
                    or last_in == "(" and i == ")" \
                    or last_in == "[" and i == "]":
                pass
            elif len(open_stack) == 0:
                return "Not balanced"
        elif len(open_stack) > 0:
            return "Not balanced"
        else:
            return "Balanced"


def main():
    print(prove_stack())


if __name__ == "__main__":
    main()
