from main import get_loader

from loader import TextCardLoader, JsonCardLoader

def test_get_loader():
    assert get_loader('.txt') == TextCardLoader, "Выбран не тот тип загрузчика для .txt"
    assert get_loader('.json') == JsonCardLoader, "Выбран не тот тип загрузчика для .json"


test_get_loader()