import pathlib
import json
import typing

from anki import Anki


class TextCardLoader:

    DEFAULT_PATH = pathlib.Path("data/words.txt")

    def __init__(self, anki: Anki, file_path: typing.Optional[pathlib.Path] = None):
        if file_path is None:
            file_path = self.DEFAULT_PATH

        self.file_path = file_path
        self.anki = anki

    def __enter__(self):
        if not self.file_path.exists():
            return
    
        with open(self.file_path, encoding='utf8') as f:
            for line in f.readlines():
                word, translation = line.split(",")
                self.anki.add_card(word, translation.strip())

    def __exit__(self, *args, **kwargs):
        with open(self.file_path, mode="w", encoding='utf8') as f:
            lines = []
            for card in self.anki.get_cards():
                line = ','.join([card.word, card.translation]) + "\n"
                lines.append(line)
            f.writelines(lines)


class JsonCardLoader:

    DEFAULT_PATH = pathlib.Path("data/words.json")

    def __init__(self, anki: Anki, file_path: typing.Optional[pathlib.Path] = None):
        if file_path is None:
            file_path = self.DEFAULT_PATH

        self.file_path = file_path
        self.anki = anki

    def __enter__(self):
        if not self.file_path.exists():
            return

        with open(self.file_path, encoding='utf8') as f:
            data = json.load(f)
            for card_data in data:
                self.anki.add_card(card_data["word"], card_data["translation"])
            

    def __exit__(self, *args, **kwargs):
        with open(self.file_path, mode="w", encoding='utf8') as f:
            json_data = []
            for card in self.anki.get_cards():
                json_data.append({"word": card.word, "translation": card.translation})
            json.dump(json_data, f, indent=4)