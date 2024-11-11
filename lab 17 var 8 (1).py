import pandas as pd
import numpy as np
import os

# Перевіряємо, чи існує файл 'matrix.csv'
if not os.path.exists('matrix.csv'):
    # Якщо файл не існує, створюємо його з випадковими даними
    print("Файл 'matrix.csv' не знайдено. Створюємо файл з випадковими даними...")
    matrix = np.random.randint(1, 10, size=(5, 5))  # створюємо матрицю 5x5 з випадкових чисел від 1 до 9
    matrix_df = pd.DataFrame(matrix)
    matrix_df.to_csv('matrix.csv', index=False, header=False)
    print("Файл 'matrix.csv' успішно створено.")

try:
    # Зчитуємо матрицю з файлу 'matrix.csv'
    matrix_df = pd.read_csv('matrix.csv', header=None)

    # Перевірка, чи є матриця квадратною
    if matrix_df.shape[0] != matrix_df.shape[1]:
        raise ValueError("Матриця не є квадратною. Переконайтеся, що кількість рядків дорівнює кількості стовпців.")

    # Обчислюємо суму елементів на головній діагоналі
    main_diag_sum = matrix_df.values.diagonal().sum()

    # Обчислюємо суму елементів на побічній діагоналі
    secondary_diag_sum = np.fliplr(matrix_df.values).diagonal().sum()

    # Зберігаємо результат у файл 'suma.txt'
    with open('suma.txt', 'w') as file:
        file.write(f"Сума головної діагоналі: {main_diag_sum}\n")
        file.write(f"Сума побічної діагоналі: {secondary_diag_sum}\n")

    print("Результати обчислень успішно збережені у файлі 'suma.txt'.")

except FileNotFoundError:
    print("Файл 'matrix.csv' не знайдено. Будь ласка, переконайтеся, що файл існує у робочій директорії.")
except ValueError as e:
    print(f"Помилка: {e}")
except Exception as e:
    print(f"Сталася несподівана помилка: {e}")
