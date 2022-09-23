from Directory import Directory
from File import File


text_files = [".txt", ".csv", ".log", ".docx"]


class Reader:
    def __init__(self, file: File):
        self.file = file

    def read(self):
        if self.file.extension in text_files:
            pass
