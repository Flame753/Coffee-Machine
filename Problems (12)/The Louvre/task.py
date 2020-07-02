class Painting:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def show(self):
        print(f'"{self.title}" by {self.artist} ({self.year}) hangs in the Louvre.')


Title = input()
Artist = input()
Year = int(input())

Painting(Title, Artist, Year).show()
