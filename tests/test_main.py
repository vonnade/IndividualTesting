from unittest import TestCase
from src.main import Movies
from src.ReadCSVFile import ReadCSVFile
from io import StringIO
from csv import reader
from unittest.mock import MagicMock


class Test(TestCase):
    def test_load_movies(self):
        expected_list = [['Dr. No', '1962', 'PAL'], ['From Russia With Love', '1963', 'PAL'], ['Goldfinger', '1964', 'NTSC'], ['Thunderball', '1965', 'PAL'], ['Diamonds Are Forever', '1971', 'NTSC'], ['Live and let Die', '1973', 'SECAM']]
        self.assertEqual(Movies.loadMovies(), expected_list)

    def test_play_movies(self):
        expected_output = "Dr. No - 1962\nFrom Russia With Love - 1963\nGoldfinger - 1964\nThunderball - 1965\nDiamonds Are Forever - 1971"
        Movies.playMovies = MagicMock(return_value="Dr. No - 1962\nFrom Russia With Love - 1963\nGoldfinger - 1964\nThunderball - 1965\nDiamonds Are Forever - 1971")
        self.assertEqual(Movies.playMovies(), expected_output)

    def test_read_csv_file(self):
        # Stub of getFileData
        def mockGetFileData():
            fileData = []
            dataFile = StringIO(
                """Title,Year,Format\nDr. No,1962,PAL\nFrom Russia With Love,1963,PAL\nGoldfinger,1964,NTSC\nThunderball,1965,PAL\nDiamonds Are Forever,1971,NTSC\nLive and let Die,1973,SECAM""")
            fileReader = reader(dataFile)
            for row in fileReader:
                if row[0] == "Title":
                    pass
                else:
                    fileData.append(row)
            return fileData

        origGetData = ReadCSVFile.getFileData("movies.csv")
        try:
            ReadCSVFile.getFileData = mockGetFileData
            expected_data = [['Dr. No', '1962', 'PAL'], ['From Russia With Love', '1963', 'PAL'],
                             ['Goldfinger', '1964', 'NTSC'], ['Thunderball', '1965', 'PAL'],
                             ['Diamonds Are Forever', '1971', 'NTSC'], ['Live and let Die', '1973', 'SECAM']]
            self.assertEqual(len(expected_data), ReadCSVFile.getDataLength())
        finally:
            ReadCSVFile.getFileData = origGetData

    def test_open_csv(self):
        # test file does not exist
        with self.assertRaises(IOError) as context:
            ReadCSVFile.getFileData("movies1.csv")
        self.assertEqual("[Errno 2] No such file or directory: '../resources/movies1.csv'", str(context.exception))
