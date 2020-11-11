class Time:
    def __init__(self):
        self._hours = 0
        self._minutes = 0
        self._seconds = 0

    # hours
    def get_hours(self):
        return self._hours

    def set_hours(self, hours):
        if hours > 23:
            hours = 23
        elif hours < 0:
            hours = 0

        self._hours = hours

    # minutes
    def get_minutes(self):
        return self._minutes

    def set_minutes(self, minutes):
        if minutes > 59:
            minutes = 59
        elif minutes < 0:
            minutes = 0

        self._minutes = minutes

    # seconds
    def get_seconds(self):
        return self._seconds

    def set_seconds(self, seconds):
        if seconds > 59:
            seconds = 59
        elif seconds < 0:
            seconds = 0

        self._seconds = seconds

    hours = property(get_hours, set_hours)
    minutes = property(get_minutes, set_minutes)
    seconds = property(get_seconds, set_seconds)

    def hours_simple(self):
        is_am = True
        if self.hours > 12:
            is_am = False
            return f"{self.hours - 12}:{self.minutes}:{self.seconds} {self.period(is_am)}"
        else:
            return f"{self.hours}:{self.minutes}:{self.seconds} {self.period(is_am)}"

    def period(self, is_am):
        if is_am:
            return "AM"
        else:
            return "PM"


def main():
    time = Time()

    hours = int(input("Hours: "))
    time.hours = hours

    minutes = int(input("Minutes: "))
    time.minutes = minutes

    seconds = int(input("Seconds: "))
    time.seconds = seconds

    print("The time is:")
    print("Hours: {}".format(time.hours))
    print("Minutes: {}".format(time.minutes))
    print("Seconds: {}".format(time.seconds))
    print(time.hours_simple())


if __name__ == "__main__":
    main()
