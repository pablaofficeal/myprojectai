# command_processor.py

from app_control import open_application, close_application
from app_control import open_application, close_application


from fl_studio_control import play_pause, toggle_recording, save_project, export_wav, export_mp3, open_playlist, open_channel_rack, open_mixer, quantize
from main import listen, speak
from system_control import set_volume, set_brightness, sleep_mode
from program_automation import select_brush, select_eraser, new_layer
from data import log_action

from app_control import open_application, close_application, list_games, open_game


from conversation import start_conversation

from app_control import (
    open_application, close_application,
    play_pause_youtube, fullscreen_youtube,
    mute_unmute_youtube, subtitles_youtube,
    increase_volume_youtube, decrease_volume_youtube
)

from speech_module import speak, listen





def process_command(command):
    if "открой" in command:
        app_name = command.split("открой ")[-1]
        open_application(app_name)

    elif "закрой" in command:
        app_name = command.split("закрой ")[-1]
        close_application(app_name)


    if "открой игру" in command:
        list_games()  # Озвучивает список игр
        game_number = listen()  # Ожидает, что пользователь назовёт номер игры, например "1"
        open_game(game_number)  # Открывает выбранную игру

    # Команды для FL Studio
    elif "включи воспроизведение" in command or "останови воспроизведение" in command:
        play_pause()

    elif "включи запись" in command or "выключи запись" in command:
        toggle_recording()

    elif "сохрани проект" in command:
        save_project()

    elif "экспорт в wav" in command:
        export_wav()

    elif "экспорт в mp3" in command:
        export_mp3()

    elif "открой плейлист" in command:
        open_playlist()

    elif "открой channel rack" in command:
        open_channel_rack()

    elif "открой микшер" in command:
        open_mixer()

    elif "квантизируй" in command:
        quantize()

    elif "поговорим" in command:
        topics = start_conversation()  # Начинаем разговор и получаем список тем
        speak("Выберите тему для разговора.")

        # Слушаем выбор темы
        command = listen()

    if "поговорим" in command:
            start_conversation()

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

    else:
        speak("Команда не распознана.")




    # Проверка на команду для открытия приложения
    if "открой" in command:
        app_name = command.split("открой ")[-1]
        open_application(app_name)
        log_action(f"Открыто приложение: {app_name}")

    # Проверка на команду для закрытия приложения
    elif "закрой" in command:
        app_name = command.split("закрой ")[-1]
        close_application(app_name)
        log_action(f"Закрыто приложение: {app_name}")

    # Установка громкости
    elif "громкость на" in command:
        try:
            volume_level = int(command.split("на ")[-1].replace("%", "").strip())
            set_volume(volume_level)
            log_action(f"Громкость установлена на {volume_level}%")
        except ValueError:
            print("Пожалуйста, укажите уровень громкости в процентах.")



    # Установка яркости
    elif "яркость на" in command:
        try:
            brightness_level = int(command.split("на ")[-1].replace("%", "").strip())
            set_brightness(brightness_level)
            log_action(f"Яркость установлена на {brightness_level}%")
        except ValueError:
            print("Пожалуйста, укажите уровень яркости в процентах.")

    # Переход в спящий режим
    elif "спящий режим" in command:
        sleep_mode()
        log_action("Переведен в спящий режим")

    #Управления браузером
     #elif "открой вкладку" in command: open_brayser()

    # Выбор кисти и ластика, новый слой
    elif "выбери кисть" in command:
        select_brush()
        log_action("Выбрана кисть")

    elif "выбери ластик" in command:
        select_eraser()
        log_action("Выбран ластик")

    elif "новый слой" in command:
        new_layer()
        log_action("Создан новый слой")


    else:print("Команда не распознана.")

