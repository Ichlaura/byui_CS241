# Lewis Lockhart :: CS-241
class Date:
    def __init__(self):
        self.month = 1
        self.day = 1
        self.year = 2020

    def prompt_validate_month(self):
        _month = int(input("Month: "))
        if _month not in range(1, 13):
            self.prompt_validate_month()
        else:
            self.month = _month

    def prompt_validate_year(self):
        _year = int(input("Year: "))
        if _year < 2000:
            self.prompt_validate_year()
        else:
            self.year = _year

    def prompt(self):
        self.day = int(input("Day: "))
        self.prompt_validate_month()
        self.prompt_validate_year()

    def display(self):
        # single digit day and month
        if self.day < 10 and self.month < 10:
            return f"0{self.month}/0{self.day}/{self.year}"
        # single digit month only
        elif self.month < 10 <= self.day:
            return f"0{self.month}/{self.day}/{self.year}"
        # single digit day only
        elif self.day < 10 <= self.month:
            return f"{self.month}/0{self.day}/{self.year}"
        # double digits - day and month
        else:
            return f"{self.month}/{self.day}/{self.year}"

    def display_long(self):
        _str_month = ""
        if self.month == 1:
            _str_month = "January"
        elif self.month == 2:
            _str_month = "February"
        elif self.month == 3:
            _str_month = "March"
        elif self.month == 4:
            _str_month = "April"
        elif self.month == 5:
            _str_month = "May"
        elif self.month == 6:
            _str_month = "June"
        elif self.month == 7:
            _str_month = "July"
        elif self.month == 8:
            _str_month = "August"
        elif self.month == 9:
            _str_month = "September"
        elif self.month == 10:
            _str_month = "October"
        elif self.month == 11:
            _str_month = "November"
        elif self.month == 12:
            _str_month = "December"

        if self.day >= 10:
            return f"{_str_month} {self.day}, {self.year}"
        else:
            return f"{_str_month} 0{self.day}, {self.year}"
