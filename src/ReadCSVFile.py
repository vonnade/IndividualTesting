import csv


class ReadCSVFile:

    @staticmethod
    def getFileData(fileName):
        fileData = []
        try:
            with open("../resources/" + fileName, 'rt') as dataFile:
                fileReader = csv.reader(dataFile)
                for row in fileReader:
                    if row[0] == "Title":
                        pass
                    else:
                        fileData.append(row)
            return fileData
        except FileNotFoundError:
            raise

    @staticmethod
    def getDataLength():
        data = ReadCSVFile.getFileData()
        return len(data)
