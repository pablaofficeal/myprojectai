import speech_recognition as sr
import pyttsx3
import webbrowser
from app_control import open_application, close_application, play_pause_youtube, fullscreen_youtube, \
    mute_unmute_youtube, subtitles_youtube, increase_volume_youtube, decrease_volume_youtube
from fl_studio_control import play_pause, toggle_recording, quantize, open_mixer, open_channel_rack, open_playlist, \
    export_mp3, export_wav, save_project
from system_control import set_volume, set_brightness, sleep_mode
from program_automation import select_brush, select_eraser, new_layer, new_sloi
from conversation import start_conversation, find_best_match  # Импорт функции поиска ответа
from google_search import search_google  # Импорт функции поиска из файла google_search.py

from app_control import open_application, close_application, list_games, open_game

# Инициализация распознавания речи и синтеза голоса
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    """Функция для прослушивания и распознавания речи"""
    with sr.Microphone() as source:
        print("Скажите команду...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language="ru-RU")
            print(f"Вы сказали: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("")
            return ""
        except sr.RequestError:
            speak("Ошибка сети.")
            return ""


def main():
    """Основной цикл работы бота"""
    speak("Бот активен. Скажите команду.")
    while True:
        command = listen()

        # Проверка на команду активации
        if "джарвис" in command:
            speak("Слушаю вас")
            command = listen()  # Слушаем следующую команду после активации

            if "начни искать" in command:
                speak("Что вы хотите найти?")
                search_command = listen()
                search_results = search_google(search_command)

                if search_results:
                    speak(f"Вот что я нашёл по запросу: {search_command}.")
                    for title, link in search_results:
                        speak(title)
                        print(title, link)  # выводим в консоль для проверки

                    # Спросим, хочет ли пользователь перейти по первой ссылке
                    speak("Хотите перейти по первой ссылке?")
                    confirmation = listen()
                    if "да" in confirmation:
                        webbrowser.open(search_results[0][1])  # Открываем первую ссылку
                        speak("Открываю ссылку.")
                    else:
                        speak("Хорошо, оставляю это.")

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

            elif"заливка" in command:
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
                speak("О чём бы вы хотели поговорить?")

                while True:
                    user_input = listen()

                    if "выход" in user_input:
                        speak("Хорошо, заканчиваю разговор.")
                        break

                    response = find_best_match(user_input)  # Ищем ответ в базе данных
                    speak(response)

            elif "выход" in command:
                speak("Завершаю работу.")
                break


if __name__ == "__main__":
    main()
