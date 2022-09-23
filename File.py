from pathlib import Path


class File:
    def __init__(self, file_route: Path):
        self.file_route = file_route.resolve()
        self.extension = self.file_route.suffix

    def __str__(self) -> str:
        return f"ruta: {self.file_route}\n" f"extension: {self.extension}"
