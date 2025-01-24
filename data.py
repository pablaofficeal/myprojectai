import datetime
import json
import os

# Путь к JSON-файлу
DB_FILE = "user_actions.json"

# Загружаем или создаём базу данных
if os.path.exists(DB_FILE):
    with open(DB_FILE, "r") as file:
        database = json.load(file)
else:
    database = {}

def log_action(action):
    """Записывает действие с датой и временем в JSON-файл"""
    timestamp = datetime.datetime.now()
    date_key = timestamp.strftime("%Y-%m-%d")
    time_value = timestamp.strftime("%H:%M:%S")

    if date_key not in database:
        database[date_key] = []
    database[date_key].append({"time": time_value, "action": action})

    # Сохраняем базу данных
    with open(DB_FILE, "w") as file:
        json.dump(database, file, indent=4)

def get_actions_for_date(date_string):
    """Возвращает действия за конкретную дату"""
    if date_string in database:
        actions = database[date_string]
        return "\n".join([f"{a['time']}: {a['action']}" for a in actions])
    return f"Нет записей за {date_string}."

def jarvis_query(query):
    """Обрабатывает запросы пользователя"""
    if "что я делал" in query.lower():
        try:
            # Извлекаем дату из вопроса
            parts = query.split()
            for part in parts:
                try:
                    # Проверяем, является ли часть датой
                    target_date = datetime.datetime.strptime(part, "%d.%m.%Y").strftime("%Y-%m-%d")
                    return get_actions_for_date(target_date)
                except ValueError:
                    continue
            return "Не могу понять дату. Укажите её в формате ДД.ММ.ГГ."
        except Exception as e:
            return f"Произошла ошибка: {e}"
    else:
        return "Не понимаю вопроса. Попробуй спросить: 'Что я делал 12.11.24?'"

# Пример использования
log_action("Написал код для логирования действий.")
log_action("Ответил на вопрос пользователя.")
print(jarvis_query("Jarvis, что я делал вчера, 12.11.24?"))
