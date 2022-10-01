from IReader import IReader
from File import File
from tika import parser
import magic


class NonTextFileReader(IReader):
    def __init__(self, force_ocr):
        self.force_ocr = force_ocr
        pass

    def read_text(self, file: File) -> str:
        if "image" not in magic.from_file(str(file.file_route), mime=True):
            return parser.from_file(str(file.file_route))["content"]
        else:
            if self.force_ocr:
                # get text from image with an OCR
                pass
