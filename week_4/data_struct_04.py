from collections import deque


class Song:
    def __init__(self):
        self.title = None
        self.artist = None

    def prompt(self):
        self.title = input("Enter the title: ")
        self.artist = input("Enter the artist: ")
        print("")

    def display(self):
        print("Playing song:")
        print(f"{self.title} by {self.artist}")
        print("")


def main():
    music_list = deque()
    continue_prompt = True

    while continue_prompt:
        print("Options:")
        print("1. Add a new song to the end of the playlist")
        print("2. Insert a new song to the beginning of the playlist")
        print("3. Play the next song")
        print("4. Quit")
        selection = int(input("Enter selection: "))
        print("")

        if selection == 1:
            s = Song()
            s.prompt()
            music_list.append(s)
        elif selection == 2:
            s = Song()
            s.prompt()
            music_list.appendleft(s)
        elif selection == 3:
            if len(music_list) == 0:
                print("The playlist is currently empty.\n")
            else:
                p = music_list.popleft()
                p.display()
        elif selection == 4:
            continue_prompt = False
            print("Goodbye")


if __name__ == "__main__":
    main()
