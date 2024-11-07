# data.py

import datetime

# Список для хранения последних действий
recent_actions = []

def log_action(action):
    """Записывает действие в список последних действий с отметкой времени"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    recent_actions.append(f"{timestamp}: {action}")
    # Если нужно, можно сохранять только последние 1000 действий
    if len(recent_actions) > 1000:
        recent_actions.pop(0)

def get_recent_actions():
    """Возвращает последние действия"""
    return recent_actions
