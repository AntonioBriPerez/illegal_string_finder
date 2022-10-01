from Directory import Directory
from File import File


text_files = [".txt", ".csv", ".log", ".docx"]


class IReader:
    def __init__(self, file: File, cadena: str) -> None:
        pass

    def read_text(
        self,
        file: File,
    ) -> str:
        pass
