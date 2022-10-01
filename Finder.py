from typing import List, Tuple
from Directory import Directory
from NonTextFileReader import NonTextFileReader
from TextFileReader import TextFileReader
from File import File


# https://stackoverflow.com/a/7392391/10509756
###################################################################################
textchars = bytearray({7, 8, 9, 10, 12, 13, 27} | set(range(0x20, 0x100)) - {0x7F})
is_binary = lambda bytes: bool(bytes.translate(None, textchars))
###################################################################################


class Finder:
    def __init__(
        self,
        directory: str,
        str_to_find: str,
        recursive=True,
        respect_case=False,
        force_ocr=False,
    ):
        self.directory = Directory(directory, recursive)
        self.cadena = str_to_find
        self.recursive = recursive
        self.respect_case = respect_case
        self.force_ocr = force_ocr

    def find(self) -> List[Tuple]:
        for f in self.directory.files:
            reader = self.__create_reader(f)
            output = (
                reader.read_text(f)
                if self.respect_case
                else reader.read_text(f).lower()
            )
            if isinstance(output, str):
                output = output.strip("\n")
                if self.cadena in output:
                    print(f"Cadena {self.cadena} encontrada! en {f}")

    def __create_reader(self, f: File):
        try:
            if not is_binary(open(str(f.file_route), "rb").read()):
                return TextFileReader()
            else:
                return NonTextFileReader(self.force_ocr)
        except Exception:
            print(f"La extension {f.extension} no esta soportada")
