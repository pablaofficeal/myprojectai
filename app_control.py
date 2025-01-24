# app_control.py

import subprocess
import os
import pyttsx3
import pyautogui
import time
import pygetwindow as gw  # Для управления окнами

engine = pyttsx3.init()


def speak(text):
    """Озвучивает текст"""
    engine.say(text)
    engine.runAndWait()


# app_control.py

import subprocess
import os
import pyttsx3

engine = pyttsx3.init()


def speak(text):
    """Озвучивает текст"""
    engine.say(text)
    engine.runAndWait()

# Список игр с номерами, названиями и путями
games = {
    "1": {"name": "Minecraft", "path": "C:\\Games\\Minecraft\\Minecraft.exe"},
    "2": {"name": "Counter Strike", "path": "C:\\Games\\CSGO\\csgo.exe"},
    "3": {"name": "Fortnite", "path": "C:\\Games\\Fortnite\\FortniteLauncher.exe"}
}

def speak(text):
    engine.say(text)
    engine.runAndWait()

def list_games():
    """Озвучивает список доступных игр"""
    speak("Хорошо, сэр, какую игру вам открыть сегодня?")
    for num, game in games.items():
        speak(f"Игра {num}: {game['name']}")

def open_game(game_number):
    """Открывает игру по номеру"""
    game = games.get(game_number)
    if game:
        subprocess.Popen([game["path"]])
        speak(f"{game['name']} открыта.")
    else:
        speak("Извините, такой игры нет в списке.")


def open_application(app_name):
    """Открывает приложение по его названию"""
    if "premiere pro" in app_name:
        subprocess.Popen(["C:\\Program Files\\Adobe\\Adobe Premiere Pro 2024\\Adobe Premiere Pro.exe"])
        speak("Adobe Premiere Pro открыт.")

    elif "figma" in app_name:
        subprocess.Popen(["C:\\Users\\pabla\\AppData\\Local\\Figma\\app-124.5.5\\Figma.exe"])
        speak("Figma открыта.")

    elif "fl" in app_name:
        subprocess.Popen(["C:\\Program Files\\Image-Line\\FL Studio 21\\FL64.exe"])
        speak("FL Studio открыта.")

    elif "ableton" in app_name or "ableton live 11" in app_name:
        subprocess.Popen(["C:\\ProgramData\\Ableton\\Live 11 Suite\\Program\\Ableton Live 11 Suite.exe"])
        speak("Ableton Live 11 открыт.")

    elif "animator" in app_name or "adobe animator" in app_name:
        subprocess.Popen(["C:\\Program Files\\Adobe\\Adobe Animate 2023\\Animate.exe"])
        speak("Adobe Animate открыт.")

    elif "тор" in app_name or "tor browser" in app_name:
        subprocess.Popen(["C:\\Users\\pabla\\Desktop\\Tor Browser\\Browser\\firefox.exe"])
        speak("Tor браузер открыт.")

    elif "android studio" in app_name:
        subprocess.Popen(["C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"])
        speak("Android Studio открыт.")

    elif "unity" in app_name:
        subprocess.Popen(["C:\\Program Files\\Unity Hub\\Unity Hub.exe"])
        speak("Unity открыт.")

    elif "visual studio" in app_name or "microsoft visual studio" in app_name:
        subprocess.Popen(["C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\Common7\\IDE\\devenv.exe"])
        speak("Microsoft Visual Studio открыт.")

    elif "whatsapp" in app_name:
        subprocess.Popen([""])
        speak("WhatsApp открыт.")

    elif "wallpaper" in app_name:
        subprocess.Popen(["C:\\Program Files\\Wallpaper Engine\\wallpaper32.exe"])
        speak("Wallpaper Engine открыт.")

    # Дополнительные ранее добавленные приложения
    elif "браузер" in app_name:
        subprocess.Popen(["C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"])
        speak("Браузер открыт.")

    elif "youtube" in app_name:
        subprocess.Popen(
            ["C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe", "https://www.youtube.com"])
        speak("YouTube открыт.")

    elif "telegram" in app_name:
        subprocess.Popen(["C:\\Users\\pabla\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"])
        speak("Telegram открыт.")

    elif "photoshop" in app_name:
        subprocess.Popen(["C:\\Program Files\\Adobe\\Adobe Photoshop 2022\\Photoshop.exe"])
        speak("Photoshop открыт.")

    elif "visual studio code" in app_name or "vscode" in app_name:
        subprocess.Popen(["C:\\Users\\pabla\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"])
        speak("Visual Studio Code открыт.")

    elif "pycharm" in app_name or "пайчарм" in app_name:
        subprocess.Popen(["I:\\PyCharm 2024.2.3\\bin\\pycharm64.exe"])
        speak("PyCharm открыт.")

    elif "блендер" in app_name:
        subprocess.Popen(["C:\\Program Files\\Blender Foundation\\Blender 4.2\\blender.exe"])
        speak("Blender открыт.")

    else:
        speak("Приложение не найдено.")


def close_application(app_name):
    """Закрывает приложение по его названию"""
    if "premiere pro" in app_name:
        os.system("taskkill /f /im Adobe Premiere Pro.exe")
        speak("Adobe Premiere Pro закрыт.")

    elif "figma" in app_name:
        os.system("taskkill /f /im Figma.exe")
        speak("Figma закрыта.")

    elif "fl" in app_name:
        os.system("taskkill /f /im FL64.exe")
        speak("FL Studio закрыта.")

    elif "ableton" in app_name or "ableton live 11" in app_name:
        os.system("taskkill /f /im Ableton Live 11 Suite.exe")
        speak("Ableton Live 11 закрыт.")

    elif "animator" in app_name or "adobe animator" in app_name:
        os.system("taskkill /f /im Animate.exe")
        speak("Adobe Animate закрыт.")

    elif "тор" in app_name or "tor browser" in app_name:
        os.system("taskkill /f /im firefox.exe")
        speak("Tor браузер закрыт.")

    elif "android studio" in app_name:
        os.system("taskkill /f /im studio64.exe")
        speak("Android Studio закрыт.")

    elif "unity" in app_name:
        os.system("taskkill /f /im Unity.exe")
        speak("Unity закрыт.")

    elif "visual studio" in app_name or "microsoft visual studio" in app_name:
        os.system("taskkill /f /im devenv.exe")
        speak("Microsoft Visual Studio закрыт.")

    elif "whatsapp" in app_name:
        os.system("taskkill /f /im WhatsApp.exe")
        speak("WhatsApp закрыт.")

    elif "wallpaper" in app_name:
        os.system("taskkill /f /im wallpaper32.exe")
        speak("Wallpaper Engine закрыт.")

    # Дополнительные ранее добавленные приложения
    elif "браузер" in app_name:
        os.system("taskkill /f /im brave.exe")
        speak("Браузер закрыт.")

    elif "telegram" in app_name:
        os.system("taskkill /f /im Telegram.exe")
        speak("Telegram закрыт.")

    elif "photoshop" in app_name:
        os.system("taskkill /f /im Photoshop.exe")
        speak("Photoshop закрыт.")

    elif "visual studio code" in app_name or "vscode" in app_name:
        os.system("taskkill /f /im Code.exe")
        speak("Visual Studio Code закрыт.")

    elif "pycharm" in app_name:
        os.system("taskkill /f /im pycharm64.exe")
        speak("PyCharm закрыт.")

    elif "блендер" in app_name:
        os.system("taskkill /f /im blender.exe")
        speak("Blender закрыт.")

    else:
        speak("Приложение не найдено.")


def activate_youtube():
    """Активирует окно YouTube, если оно открыто"""
    try:
        window = gw.getWindowsWithTitle("YouTube")[0]
        window.activate()
        time.sleep(0.5)
    except IndexError:
        speak("Окно YouTube не найдено.")


def play_pause_youtube():
    """Включает или приостанавливает видео на YouTube"""
    pyautogui.press("space")
    speak("Воспроизведение/пауза на YouTube.")

def fullscreen_youtube():
    """Включает или выключает полноэкранный режим на YouTube"""
    pyautogui.press("f")
    speak("Полноэкранный режим на YouTube.")

def mute_unmute_youtube():
    """Включает или выключает звук на YouTube"""
    pyautogui.press("m")
    speak("Звук на YouTube переключен.")

def subtitles_youtube():
    """Включает или выключает субтитры на YouTube"""
    pyautogui.press("c")
    speak("Субтитры на YouTube переключены.")

def increase_volume_youtube():
    """Увеличивает громкость на YouTube"""
    pyautogui.press("up")
    speak("Громкость на YouTube увеличена.")

def decrease_volume_youtube():
    """Уменьшает громкость на YouTube"""
    pyautogui.press("down")
    speak("Громкость на YouTube уменьшена.")