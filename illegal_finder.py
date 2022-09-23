from Finder import Finder


def main():
    f = Finder("/home/antonio/Escritorio", "cadena", recursive=True)
    print(f.find())


if __name__ == "__main__":
    main()
