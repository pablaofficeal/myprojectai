# fl_studio_control.py

import pyttsx3
import pyautogui

engine = pyttsx3.init()

def speak(text):
    """Озвучивает текст"""
    engine.say(text)
    engine.runAndWait()

# Функции для управления FL Studio
def play_pause():
    """Воспроизведение или пауза"""
    pyautogui.press('space')
    speak("Воспроизведение или пауза включены.")

def toggle_recording():
    """Включить или выключить запись"""
    pyautogui.press('r')
    speak("Запись включена или выключена.")

def save_project():
    """Сохранить проект"""
    pyautogui.hotkey('ctrl', 's')
    speak("Проект сохранен.")

def export_wav():
    """Экспорт проекта в WAV"""
    pyautogui.hotkey('ctrl', 'r')
    speak("Проект экспортирован в WAV.")

def export_mp3():
    """Экспорт проекта в MP3"""
    pyautogui.hotkey('ctrl', 'shift', 'r')
    speak("Проект экспортирован в MP3.")

def open_playlist():
    """Открыть или закрыть плейлист"""
    pyautogui.press('f5')
    speak("Плейлист открыт или закрыт.")

def open_channel_rack():
    """Открыть или закрыть Channel Rack"""
    pyautogui.press('f6')
    speak("Channel Rack открыт или закрыт.")

def open_mixer():
    """Открыть или закрыть микшер"""
    pyautogui.press('f9')
    speak("Микшер открыт или закрыт.")

def quantize():
    """Быстрое квантизирование в пианино-ролле"""
    pyautogui.hotkey('ctrl', 'q')
    speak("Быстрое квантизирование выполнено.")
