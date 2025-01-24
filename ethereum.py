import os


import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
from torch.utils.data.datapipes.dataframe import dataframes

# Функция для загрузки нескольких файлов
def load_multiple_files(directory):
    all_data = []
    # Проходим по всем файлам в директории
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):  # Проверяем, что это CSV файл
            file_path = os.path.join(directory, filename)
            data = pd.read_csv(file_path)  # Загружаем данные из файла
            all_data.append(data)  # Добавляем данные в список
    # Объединяем все данные в один DataFrame
    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df  # Этот return теперь внутри функции


# Функция для статистики
def get_statistics(df):
    stats = {
        'Средняя цена открытия': df['Open'].mean(),
        'Максимальная цена открытия': df['Open'].max(),
        'Минимальная цена открытия': df['Open'].min(),
        'Общее количество записей': len(df)
    }
    return stats

# Функция для построения прогноза
def make_predictions(df, target_column='Open', feature_columns=None):
    if feature_columns is None:
        feature_columns = ['Record Date', 'Country - Currency Description', 'Exchange Rate', 'Effective Date']

    # Убираем строки с пропущенными значениями
    df = df.dropna(subset=feature_columns + [target_column])

    # Делим данные на обучающую и тестовую выборки
    X = df[feature_columns]
    y = df[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Модель линейной регрессии
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Прогнозируем на тестовых данных
    predictions = model.predict(X_test)
    accuracy = model.score(X_test, y_test)

    return predictions, accuracy

