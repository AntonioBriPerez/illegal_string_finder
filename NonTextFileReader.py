from IReader import IReader
from File import File
from tika import parser


class NonTextFileReader(IReader):
    def __init__(self):
        pass

    def read_text(self, file: File) -> str:
        return parser.from_file(str(file.file_route))["content"]
