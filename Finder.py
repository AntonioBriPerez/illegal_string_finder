from typing import List, Tuple
from Directory import Directory
from Reader import Reader


class Finder:
    def __init__(self, directory: str, string: str, recursive):
        self.directory = Directory(directory, recursive)
        self.string = string
        self.recursive = recursive

    def find(self) -> List[Tuple]:
        for f in self.directory.files:
            reader = Reader(f)
            print(f)
