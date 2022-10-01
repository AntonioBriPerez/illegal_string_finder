from glob import iglob
from File import File
from pathlib import Path


class Directory:
    def __init__(self, dir_route: str, recursive):
        self.dir_route = Path(dir_route)
        if not self.dir_route.exists():
            raise ValueError(f"{self.dir_route} no existe")

        self.recursive = recursive
        self.files = self.__init_dir_files()

    def __init_dir_files(self):
        return [File(f) for f in self.dir_route.rglob("*.*") if f.is_file()]
