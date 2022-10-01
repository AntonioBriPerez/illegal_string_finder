from Finder import Finder


def main():
    f = Finder(
        "/home/antonio/Escritorio/ii-god",
        str_to_find="hola",
        recursive=True,
        respect_case=True,
        force_ocr = False
    )
    
    print(f.find())


if __name__ == "__main__":
    main()
