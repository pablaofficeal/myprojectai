from command_processor import process_command
from data import get_recent_actions


def main() -> object:
    """Основной цикл работы бота"""
    speak("Бот активен. Скажите команду.")
    while True:
        command = listen()

        if "джарвис" in command:
            speak("Слушаю вас")
            command = listen()
            process_command(command)

            # Пример использования истории действий
            if "покажи последние действия" in command:
                actions = get_recent_actions()
                for action in actions:
                    speak(action)

        elif "выход" in command:
            speak("Завершаю работу.")
            break


if __name__ == "__main__":
    main()


def listen():
    return None


def speak():
    return None