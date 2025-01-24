import requests

# Функция для получения данных
def get_concept_data(concept):
    url = f"http://api.conceptnet.io/c/en/{concept}"  # Формируем запрос
    response = requests.get(url)  # Отправляем запрос
    data = response.json()  # Получаем данные в формате JSON
    return data

# Пример запроса для слова "dog"
concept = "dog"
data = get_concept_data(concept)

# Печатаем ответ
print(data)
