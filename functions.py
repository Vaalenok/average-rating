import csv
import os

def read_files(files):
    data = []

    for file in files:
        if not os.path.isfile(file):
            print(f"Ошибка: файл '{file}' не найден")
            continue

        if not file.lower().endswith('.csv'):
            print(f"Ошибка: файл '{file}' не является CSV")
            continue

        with open(file, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            if reader.fieldnames is None:
                print(f"Ошибка: файл '{file}' не содержит заголовков CSV.")
                continue

            for row in reader:
                data.append(row)

    return data
