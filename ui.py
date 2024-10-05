import textwrap

from anki import Anki


class TextUI:

    MENU = textwrap.dedent("""
        1. Добавить слова
        2. Начать играть
        3. Вывести список слов
        4. Найти перевод
        5. Выйти
    """)
    def __init__(self, anki: Anki):
        self.anki = anki

    def add_cards(self):
        print("Ввод слов! (/exit для выхода)")
        while True:
            word = input("Введите слово: ")
            if word == "/exit":
                break
            translated_word = input("Введите перевод слова: ")
            self.anki.add_card(word, translated_word)

    def guess_word(self):
        print("Перевод слов! (/exit для выхода)")
        while True:
            # 1. Выбрать случайное слово и вывести его на экран
            card = self.anki.get_random_card()
            print("Переведите слово:")
            print(card.word, "= ", end="")
            # 2. Получить от пользователя перевод
            translation = input()
            if translation == "/exit":
                break
            # 3. Проверить ввод пользователя на корректность
            if translation == card.translation:
                print("Все верно!")
            else:
                print("Нет, не верно :(")
    
    def print_cards(self):
        cards = self.anki.get_cards()
        for card in cards:
            print(card.word, "->", card.translation)

    def find_translation(self):
        word = input("Введите слово: ")
        try:
            card = self.anki.get_card(word)
        except ValueError:
            print("Перевод не найден")
        else:
            print(f"Перевод: {card.translation}")

    def mainloop(self):
        # Запрашивает ввод пользователя
        # Реагирует на него.
        while True:
            choice = input(f"Выберите, что вы хотите сделать:\n{self.MENU}")
            if choice == "1":
                self.add_cards()
            elif choice == "2":
                self.guess_word()
            elif choice == "3":
                self.print_cards()
            elif choice == "4":
                self.find_translation()
            elif choice == "5":
                break
            else:
                print("Выберите корректный пункт меню = [1, 2, 3, 4, 5]")
