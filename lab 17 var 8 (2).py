import pandas as pd
import os
import json
from datetime import datetime

# Перевіряємо, чи існує файл 'pupils.json'
if not os.path.exists('pupils.json'):
    # Якщо файл не існує, створюємо його з випадковими даними
    print("Файл 'pupils.json' не знайдено. Створюємо файл з випадковими даними...")
    data = [
        {"name": "Іван Іванов", "birthdate": "2005-04-15"},
        {"name": "Марія Петренко", "birthdate": "2004-09-10"},
        {"name": "Олег Сидоренко", "birthdate": "2003-11-22"},
    ]
    with open('pupils.json', 'w') as f:
        json.dump(data, f)
    print("Файл 'pupils.json' успішно створено.")

try:
    # Зчитуємо дані з файлу 'pupils.json'
    pupils_df = pd.read_json('pupils.json')

    # Перевірка, чи є у файлі потрібні колонки
    if 'birthdate' not in pupils_df.columns:
        raise ValueError("Файл 'pupils.json' не містить колонки 'birthdate'.")

    # Створюємо Series з даних про дати народження
    birthdates_series = pd.Series(pupils_df['birthdate'])

    # Витягуємо роки народження
    years_series = birthdates_series.apply(lambda x: pd.to_datetime(x).year)

    # Зберігаємо результат у файл 'years.json'
    years_series.to_json('years.json', orient='values')
    print("Роки народження успішно збережені у файлі 'years.json'.")

except FileNotFoundError:
    print("Файл 'pupils.json' не знайдено. Будь ласка, переконайтеся, що файл існує у робочій директорії.")
except ValueError as e:
    print(f"Помилка: {e}")
except Exception as e:
    print(f"Сталася несподівана помилка: {e}")
