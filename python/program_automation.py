# program_automation.py

import pyttsx3
import pyautogui
import time

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def select_brush():
    """Выбирает инструмент 'Кисть' в Photoshop"""
    try:
        pyautogui.hotkey('b')  # Обычно 'B' — горячая клавиша для выбора кисти
        speak("Инструмент 'Кисть' выбран")
    except Exception as e:
        speak(f"Ошибка при выборе кисти: {str(e)}")

def select_eraser():
    """Выбирает инструмент 'Ластик' в Photoshop"""
    try:
        pyautogui.hotkey('e')  # Обычно 'E' — горячая клавиша для ластика
        speak("Инструмент 'Ластик' выбран")
    except Exception as e:
        speak(f"Ошибка при выборе ластика: {str(e)}")

def new_layer():
    """Создает новый слой в Photoshop"""
    try:
        pyautogui.hotkey('shift', 'ctrl', 'n')  # Shift + Ctrl + N — горячая клавиша для нового слоя
        time.sleep(0.5)
        pyautogui.press('enter')  # Подтверждаем создание слоя
        speak("Новый слой создан")
    except Exception as e:
        speak(f"Ошибка при создании нового слоя: {str(e)}")

def new_sloi():
    """Создает новый слой в Photoshop"""
    try:
        pyautogui.hotkey('shift', 'f5')
        time.sleep(0.5)
        pyautogui.press('enter')  # Подтверждаем создание слоя
        speak("Выполняю заливку")
    except Exception as e:
        speak(f"Ошибка при заливке: {str(e)}")
