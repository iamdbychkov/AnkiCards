import argparse

import pathlib

from anki import Anki
from ui import TextUI
from loader import TextCardLoader, JsonCardLoader


def get_loader(extension: str) -> type[TextCardLoader] | type[JsonCardLoader]:
    if extension == '.txt':
        loader = TextCardLoader
    elif extension == '.json':
        loader = JsonCardLoader
    else:
        raise ValueError(f'Unknown file format {extension}')
    return loader


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='Путь до файла с карточками')
    args = parser.parse_args()

    filepath = pathlib.Path(args.filepath)

    loader = get_loader(filepath.suffix)

    anki = Anki()

    with loader(anki, filepath):
        ui = TextUI(anki)
        ui.mainloop()


if __name__ == '__main__':
    main()
