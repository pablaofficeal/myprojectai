import json

# Функция для загрузки данных из файла базы данных
def load_data(filename="guesser_data.json"):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден!")
        return []

# Функция для добавления нового персонажа в базу данных
def add_character(data, name, character_type, questions):
    new_character = {
        "name": name,
        "type": character_type,
        "questions": questions
    }
    data.append(new_character)
    return data

# Функция для сохранения данных в файл базы данных
def save_data(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
