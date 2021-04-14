# TSI Individual Testing Submission
## Introduction

This is a basic program that imports movies from a CSV, which then checks if it can play the video on the defined TV. As it is a British TV it would normally only allow PAL content. So, I created an Adapter that converts the signal from NTSC to PAL. Any other format will be rejected.

## Link to class with the data load functions to be doubled

- [ReadCSVFile.getFileData](src/ReadCSVFile.py) is doubled when testing.
- [movies.csv](resources/movies.csv) is the load file.

## List the functions that can be double

1. [ReadCSVFile.getFileData](src/ReadCSVFile.py)
2. [main.loadMovies](src/main.py)
3. [main.playMovies](src/main.py)

## Link to class with unit tests

[test_main.Test](tests/test_main.py)

## List names of unit tests methods for stub, mock and fake

### Unit Tests

1. test_load_movies
2. test_play_movies

### Doubling stub

1. test_read_csv_file

### Mock

1. test_open_csv
