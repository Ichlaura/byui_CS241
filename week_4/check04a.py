# Lewis Lockhart :: CS-241
class Person:
    """ Person class has a name and year, with a display() """
    def __init__(self):
        self.name = "anonymous"
        self.year = "unknown"

    def __str__(self):
        print("Person class used for book authors.")
        print("Defaults: name=anonymous, year=unknown")

    def display(self):
        return f"{self.name} (b. {self.year})"


class Book:
    """
    Book class has a title, author, and publisher.
    It also has a display().
    """
    def __init__(self):
        self.title = "untitled"
        self.author = Person()
        self.publisher = "unpublished"

    def __str__(self):
        print("Book class: Has a title, author, and publisher.")

    def display(self):
        print(self.title)
        print("Publisher:")
        print(self.publisher)
        print("Author:")
        print(self.author.display())


def main():
    """ Main() instantiates Book() and prompts the user for input. """
    # Create a new book
    bk = Book()
    # Call that book's display function
    bk.display()
    # Prompts the user for each of the following: author name and birth year,
    # and the books title and publisher.
    print('')
    print("Please enter the following:")
    bk.author.name = input("Name: ")
    bk.author.year = input("Year: ")
    bk.title = input("Title: ")
    bk.publisher = input("Publisher: ")
    # Call that book's display function
    print('')
    bk.display()


# If this is the main program being run, call our main function above
if __name__ == "__main__":
    main()
