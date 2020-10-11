# Lewis Lockhart :: CS-241
from assignment import Assignment


def main():
    a = Assignment()
    a.prompt()
    a.display()
    print(a.start_date.display_long())


if __name__ == "__main__":
    main()
