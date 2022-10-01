from pathlib import Path
from IReader import IReader
from File import File


class TextFileReader(IReader):
    def __init__(self):
        pass

    def read_text(self, file: File) -> str:
        return file.file_route.read_text(encoding="ISO-8859-1")
