# system_control.py

import os
import pyttsx3
import screen_brightness_control as sbc

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def set_volume(level):
    """Устанавливает громкость системы на указанный уровень (от 0 до 100)"""
    try:
        os.system(f"nircmd.exe setsysvolume {level * 65535 // 100}")
        speak(f"Громкость установлена на {level}%")
    except Exception as e:
        speak(f"Ошибка при установке громкости: {str(e)}")

def set_brightness(level):
    """Устанавливает яркость экрана на указанный уровень (от 0 до 100)"""
    try:
        sbc.set_brightness(level)
        speak(f"Яркость установлена на {level}%")
    except Exception as e:
        speak(f"Ошибка при изменении яркости: {str(e)}")

def sleep_mode():
    """Переводит компьютер в спящий режим"""
    try:
        speak("Перевожу компьютер в спящий режим")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    except Exception as e:
        speak(f"Ошибка при переводе в спящий режим: {str(e)}")
