import cv2
import numpy as np
import mss
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Функция захвата экрана
def capture_screen():
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        screenshot = sct.grab(monitor)
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        return img

# Функция анализа содержимого экрана
def analyze_screen():
    img = capture_screen()
    # Пример анализа — распознавание лиц
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        speak("На экране обнаружены лица.")
    else:
        speak("На экране не обнаружено лиц.")
    return img

# Функция начала обучения
def start_learning():
    speak("Начинаю обучение на данных с экрана.")
    # Здесь можно добавить логику для обучения модели
    # Например, запись кадров или использование данных для тренировки модели
