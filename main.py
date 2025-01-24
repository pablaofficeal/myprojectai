import pyautogui
import speech_recognition as sr
import pyttsx3
import webbrowser
import cv2
import ethereum
import random

from app_control import open_application, close_application, play_pause_youtube, fullscreen_youtube, \
    mute_unmute_youtube, subtitles_youtube, increase_volume_youtube, decrease_volume_youtube
from fl_studio_control import play_pause, toggle_recording, quantize, open_mixer, open_channel_rack, open_playlist, \
    export_mp3, export_wav, save_project
from system_control import set_volume, set_brightness, sleep_mode
from program_automation import select_brush, select_eraser, new_layer, new_sloi
from conversation import start_conversation, find_best_match
from googleapiclient.discovery import build
from app_control import open_application, close_application, list_games, open_game
from command_list import list_commands
from video_control import capture_screen, analyze_screen, start_learning
from learning_control import start_learning, replay_actions
from data import log_action, jarvis_query

# Инициализация распознавания речи и синтеза голоса
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Добавление функции для поиска в Google
API_KEY = "AIzaSyDFUhb3Mr5vEIEPa9AfqO7khVO1mvp8khY"
CX_ID = "731ef735025184a2c"

def search_google(query, num_results=5):
    try:
        service = build("customsearch", "v1", developerKey=API_KEY)
        res = service.cse().list(q=query, cx=CX_ID, num=num_results).execute()
        results = res.get("items", [])
        if not results:
            return "По вашему запросу ничего не найдено."
        response = []
        for item in results:
            response.append(f"{item['title']}: {item['link']}")
        return "\n".join(response)
    except Exception as e:
        return f"Ошибка при выполнении поиска: {e}"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Скажите команду...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language="ru-RU")
            print(f"Вы сказали: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak(".")
            return ""
        except sr.RequestError:
            speak("Ошибка сети.")
            return ""

def analyze_statistics():
    speak("Загружаю данные для анализа...")
    try:
        df = ethereum.load_multiple_files('H:\\111my jarvis my python project jarvis\\pythonProject2\\ethereum_data/')
        if df.empty:
            raise ValueError("Загруженные данные пусты.")
        stats = ethereum.get_statistics(df)
    except Exception as e:
        speak(f"Ошибка: {e}")
        print(f"Ошибка: {e}")

def make_predictions():
    speak("Загружаю данные для прогнозов...")
    try:
        # Загрузка данных из файла (укажи правильный путь)
        df = ethereum.load_multiple_files('H:\\111my jarvis my python project jarvis\\pythonProject2\\ethereum_data/')
        predictions, accuracy = ethereum.make_predictions(df)
        speak(f"Прогнозы построены. Точность модели: {accuracy:.2f}")
        print(predictions[:5])  # Показать первые 5 прогнозов в консоли
    except Exception as e:
        speak("Не удалось выполнить прогнозы.")
        print(f"Ошибка: {e}")

# Функция для игры
def guess_who_am_i(character_data=None):
    character = random.choice(character_data)
    name = character["name"]
    description = character["description"]

    speak("Я загадал персонажа. Ты должен угадать кто это. Вот подсказка: ")
    speak(description)

    attempts = 3  # Количество попыток
    while attempts > 0:
        guess = listen()
        if guess.lower() == name.lower():
            speak(f"Поздравляю, ты угадал! Это {name}.")
            break
        else:
            attempts -= 1
            speak(f"Неправильно. У тебя осталось {attempts} попыток.")

    if attempts == 0:
        speak(f"Ты не угадал. Это был {name}.")
    speak("Хотите сыграть ещё раз?")

# Функция для повторной игры или завершения
def play_guess_game():
    while True:
        speak("Хотите сыграть в 'Угадай, кто я'? (Да/Нет)")
        response = listen().lower()
        if "да" in response:
            guess_who_am_i()
        else:
            speak("Хорошо, возвращаюсь к основным функциям.")
            break

def main():
    speak("Здравствуйте сэр, меня зовут Джарвис, приступим к работе")
    while True:
        command = listen()

        if "джарвис ты тут" in command or "джарвис" in command:
            speak("Да, сэр, слушаю вас")
            command = listen()

            # Логируем команды пользователя
            log_action(f"Команда: {command}")

            # Обработка команды для анализа статистики
            if "посмотри статистику" in command:
                analyze_statistics()

            # Обработка команды для прогнозов
            elif "сделай прогнозы" in command:
                make_predictions()

            # Обработка команды для игры
            elif 'угадай кто я' in command:
                play_guess_game()

            # Логируем команды пользователя
            log_action(f"Команда: {command}")

            # Обработка команды для поиска в интернете
            if "найди в интернете" in command:
                speak("Что вы хотите найти?")
                query = listen()  # Слушаем запрос пользователя
                if query:
                    speak(f"Ищу в Google: {query}")
                    search_results = search_google(query)  # Получаем результаты поиска
                    speak("Вот что я нашел:")
                    print(search_results)  # Печатает результаты в консоли
                    speak(search_results)  # Зачитывает результаты поиска

            # Обработка команды для записи действия
            elif "запиши действие" in command:
                speak("Что записать?")
                action = listen()
                log_action(action)
                speak("Действие записано.")

            # Команда для обучения
            elif "начни обучаться" in command:
                start_learning()
                speak("Я начал обучение.")

            # Команда для воспроизведения действий
            elif "повтори действия" in command:
                replay_actions()
                speak("Воспроизвожу ваши действия.")

            # Другие команды (открытие приложений, управление громкостью и т.д.)
            elif "открой" in command:
                app_name = command.split("открой ")[-1]
                open_application(app_name)

            elif "закрой" in command:
                app_name = command.split("закрой ")[-1]
                close_application(app_name)

            elif "громкость на" in command:
                try:
                    volume_level = int(command.split("на ")[-1].replace("%", "").strip())
                    set_volume(volume_level)
                except ValueError:
                    speak("Пожалуйста, укажите уровень громкости в процентах.")

            elif "яркость на" in command:
                try:
                    brightness_level = int(command.split("на ")[-1].replace("%", "").strip())
                    set_brightness(brightness_level)
                except ValueError:
                    speak("Пожалуйста, укажите уровень яркости в процентах.")

            # Обработка команды для открытия игры
            if "открой игру" in command:
                list_games()  # Озвучивает список игр
                speak("Выберите номер игры.")
                game_number = listen()  # Слушаем номер игры, который скажет пользователь
                open_game(game_number)  # Открывает выбранную игру

            elif "спящий режим" in command:
                sleep_mode()

            elif "кисть" in command:
                select_brush()

            elif "ластик" in command:
                select_eraser()

            elif "заливка" in command:
                new_sloi()

            elif "новый слой" in command:
                new_layer()

            # Команды для FL Studio
            elif "включи воспроизведение" in command or "останови воспроизведение" in command:
                play_pause()

            elif "включи запись" in command or "выключи запись" in command:
                toggle_recording()

            elif "сохрани проект" in command:
                save_project()

            elif "wav" in command:
                export_wav()

            elif "mp3" in command:
                export_mp3()

            elif "лист" in command:
                open_playlist()

            elif "открой channel rack" in command:
                open_channel_rack()

            elif "микшер" in command:
                open_mixer()

            elif "квантизируй" in command:
                quantize()

            # Команды для управления YouTube
            elif "включи видео" in command or "останови видео" in command:
                play_pause_youtube()

            elif "полный экран" in command:
                fullscreen_youtube()

            elif "выключи звук" in command or "включи звук" in command:
                mute_unmute_youtube()

            elif "субтитры" in command:
                subtitles_youtube()

            elif "увеличь громкость" in command:
                increase_volume_youtube()

            elif "уменьши громкость" in command:
                decrease_volume_youtube()

            # Команда для начала разговора с поиском ответа из базы данных
            elif "поговорим" in command:
                speak("да сэр о, чём бы вы хотели поговорить?")

                while True:
                    user_input = listen()

                    if "выход" in user_input:
                        speak("да сэр")
                        break

                    response = find_best_match(user_input)  # Ищем ответ в базе данных
                    speak(response)

            elif "выход" in command:
                speak("да сэр выхожу.")
                break



if __name__ == "__main__":
    main()
