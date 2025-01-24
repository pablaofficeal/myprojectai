# conversation.py
import json
from difflib import get_close_matches
import pyttsx3

engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


# Загрузка базы данных
with open('conversation_data.json', 'r', encoding='utf-8') as f:
    conversation_data = json.load(f)


def find_best_match(user_input):
    """Ищет лучший ответ на вопрос пользователя"""
    questions = [item['question'] for item in conversation_data]
    matches = get_close_matches(user_input, questions, n=1, cutoff=0.5)  # Ищет лучший подходящий вопрос

    if matches:
        best_match = matches[0]
        for item in conversation_data:
            if item['question'] == best_match:
                return item['answer']
    return "Извините, я пока не знаю, как на это ответить."


def start_conversation():
    """Начинает разговор и обрабатывает вопросы пользователя"""
    speak("О чём бы ты хотел поговорить?")
    while True:
        user_input = input("Вы: ")  # Можно заменить на `listen()` для голосового ввода
        if "выход" in user_input:
            speak("Хорошо, заканчиваю разговор.")
            break
        else:
            response = find_best_match(user_input)
            speak(response)
