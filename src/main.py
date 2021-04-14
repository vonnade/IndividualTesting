from src.ReadCSVFile import ReadCSVFile
import sys
from io import StringIO


# Interface
class ColourInterface:
    def kind(self): pass

    def frequency(self): pass

    def lines(self): pass

    def fps(self): pass


# Adaptee
class Encoder(ColourInterface):
    def kind(self):
        return "PAL"

    def frequency(self):
        return 50

    def lines(self):
        return 625

    def fps(self):
        return 25


# The Adapter (which defines NTSC requirements)
class Adapter(ColourInterface):
    __encoder = None

    def __init__(self, encoder):
        self.__encoder = encoder

    def kind(self):
        return "NTSC"

    def frequency(self):
        return 60

    def lines(self):
        return 525

    def fps(self):
        return 29.97


# Client
class TV:
    __power = None

    def __init__(self, power):
        self.__power = power

    def play_video(self):
        if self.__power.kind() == "PAL" and self.__power.frequency() == 50 and self.__power.lines() == 625 and self.__power.fps() == 25:
            return 1
        elif self.__power.kind() == "NTSC" and self.__power.frequency() == 60 and self.__power.lines() == 525 and self.__power.fps() == 29.97:
            return 1
        else:
            return 0


class Movies:

    @staticmethod
    def loadMovies():
        readCSVFile = ReadCSVFile()
        movieData = readCSVFile.getFileData("movies.csv")
        return movieData

    @staticmethod
    def playMovies():
        movieData = Movies.loadMovies()
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        unplayable_movies = 0
        for movie in movieData:
            if movie[2] == "PAL":
                encoder = Encoder()
                tv = TV(encoder)
                if tv.play_video():
                    print(movie[0] + " - " + movie[1])
            elif movie[2] == "NTSC":
                encoder = Encoder()
                adapter = Adapter(encoder)
                tv = TV(adapter)
                if tv.play_video():
                    print(movie[0] + " - " + movie[1])
            else:
                unplayable_movies += 1
        sys.stdout = sys.__stdout__
        console_output = capturedOutput.getvalue()
        print(f"===========\nTotal movies not playable: {unplayable_movies}")
        print("Playable Movies:\n")
        return console_output


def main():
    print(Movies.playMovies())
    return 0


if __name__ == "__main__":
    main()
