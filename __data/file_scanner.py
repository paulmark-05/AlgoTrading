import os


class FileScanner:

    @staticmethod
    def scan(folder):

        files = []

        for file in os.listdir(folder):

            if file.endswith(".csv"):

                files.append(file)

        return files