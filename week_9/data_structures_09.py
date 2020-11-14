"""
Assignment: week 9 data structures
Author: Lewis Lockhart
"""


edu_lev_count = {
    "Preschool": 0,
    "1st-4th": 0,
    "5th-6th": 0,
    "7th-8th": 0,
    "9th": 0,
    "10th": 0,
    "11th": 0,
    "12th": 0,
    "HS-grad": 0,
    "Some-college": 0,
    "Assoc-voc": 0,
    "Assoc-acdm": 0,
    "Bachelors": 0,
    "Prof-school": 0,
    "Masters": 0,
    "Doctorate": 0
}


def process_data():
    with open("cen.csv", "r") as file_to_process:

        for line in file_to_process:
            edu = line.split(",")[3].strip()
            edu_lev_count[edu] += 1


def main():
    process_data()
    for c, n in edu_lev_count.items():
        print(f"{n} -- {c}")


if __name__ == "__main__":
    main()
