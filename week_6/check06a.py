"""
File: check05a.py
By: Lewis Lockhart
"""


class Book:
    """
    Creates basic book object.
    """
    def __init__(self):
        self.title = ""
        self.author = ""
        self.publication_year = 0

    def prompt_book_info(self):
        """ Prompts for book info. """
        self.title = input("Title: ")
        self.author = input("Author: ")
        self.publication_year = input("Publication Year: ")

    def display_book_info(self):
        """ Displays book info. """
        print(f"{self.title} ({self.publication_year}) by {self.author}")


class TextBook(Book):
    """
    Creates textbook object.
    """
    def __init__(self):
        # extends Book()
        self.subject = ""
        super().__init__()

    def prompt_subject(self):
        """ Prompts for book subject. """
        self.subject = input("Subject: ")

    def display_subject(self):
        """ Displays book subject. """
        print(f"Subject: {self.subject}")


class PictureBook(Book):
    """
    Creates pictureBook object.
    """
    def __init__(self):
        self.illustrator = ""
        super().__init__()

    def prompt_illustrator(self):
        """ Prompts for book illustrator. """
        self.illustrator = input("Illustrator: ")

    def display_illustrator(self):
        """ Displays book illustrator. """
        print(f"Illustrator: {self.illustrator}")


def main():
    # create a book obj and call methods
    book = Book()
    book.prompt_book_info()
    print('')
    book.display_book_info()
    print('')

    # create a textbook obj and call methods
    t_book = TextBook()
    t_book.prompt_book_info()
    t_book.prompt_subject()
    print('')
    t_book.display_book_info()
    t_book.display_subject()
    print('')

    # create a picture book obj and call methods
    p_book = PictureBook()
    p_book.prompt_book_info()
    p_book.prompt_illustrator()
    print('')
    p_book.display_book_info()
    p_book.display_illustrator()


if __name__ == "__main__":
    main()

