import pyautogui
import time
import cv2
import numpy as np
import mss
import json
import os
import subprocess

from video_control import capture_screen

# Запись действий
actions = []

# Функция для записи действий
def record_action(action_type, app_name=None, position=None, key=None, path=None):
    action = {
        "type": action_type,
        "app_name": app_name,
        "timestamp": time.time(),
        "position": position,
        "key": key,
        "path": path
    }
    actions.append(action)

# Функция для открытия приложений
def open_application(app_name):
    if app_name == "visual studio code":
        subprocess.Popen(["code"])
        record_action("open_app", app_name="visual studio code")
    elif app_name == "fl studio":
        subprocess.Popen(["C:\\Program Files\\Image-Line\\FL Studio 21\\FL64.exe"])  # Замените на путь к FL Studio
        record_action("open_app", app_name="fl studio")

# Функция создания папки
def create_folder(path):
    os.makedirs(path, exist_ok=True)
    record_action("create_folder", path=path)

# Функция для взаимодействия с Visual Studio Code
def interact_with_vscode(action):
    if action["type"] == "create_file":
        pyautogui.hotkey("ctrl", "n")  # Создаёт новый файл
    elif action["type"] == "save_file":
        pyautogui.hotkey("ctrl", "s")  # Сохранение файла
    elif action["type"] == "open_file":
        pyautogui.hotkey("ctrl", "o")  # Открытие файла

# Функция для взаимодействия с FL Studio
def interact_with_flstudio(action):
    if action["type"] == "save_project":
        pyautogui.hotkey("ctrl", "s")  # Сохранение проекта
    elif action["type"] == "new_project":
        pyautogui.hotkey("ctrl", "n")  # Новый проект

# Функция создания файла
def create_file(path):
    with open(path, "w") as f:
        f.write("")  # Создаёт пустой файл
    record_action("create_file", path=path)

# Основная функция для начала обучения
def start_learning():
    print("Джарвис начал обучение...")
    app_name = None
    start_time = time.time()

    try:
        while time.time() - start_time < 150:
            screen = capture_screen()
            current_app = pyautogui.getActiveWindowTitle()

            if current_app != app_name:
                app_name = current_app
                record_action("switch_app", app_name=app_name)
            time.sleep(1)
    except KeyboardInterrupt:
        pass

    print("Обучение завершено. Данные сохранены.")
    save_actions()

# Сохранение действий
def save_actions():
    with open("actions.json", "w") as f:
        json.dump(actions, f, indent=4)

# Воспроизведение действий
def replay_actions():
    print("Воспроизвожу действия...")
    with open("actions.json", "r") as f:
        actions_to_replay = json.load(f)

    for action in actions_to_replay:
        if action["type"] == "open_app" and action["app_name"]:
            open_application(action["app_name"])
        elif action["type"] == "create_folder" and action["path"]:
            create_folder(action["path"])
        elif action["type"] == "create_file" and action["path"]:
            create_file(action["path"])
        elif action["type"] == "click" and action["position"]:
            pyautogui.click(action["position"])
        elif action["type"] == "keypress" and action["key"]:
            pyautogui.press(action["key"])
        time.sleep(0.5)
