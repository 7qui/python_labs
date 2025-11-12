import csv
import json
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный.
    """

    json_path = Path(json_path)

    if json_path.exists() == False:
        raise FileNotFoundError

    if len(json_path.read_text(encoding="utf-8")) <= 0:
        raise ValueError

    with json_path.open("r", newline="", encoding='utf-8') as f:
        json_import = json.load(f)

    csv_path = Path(csv_path)

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        csv_writer = csv.DictWriter(f, fieldnames=["name", 'age', 'city'])

        csv_writer.writeheader()
        csv_writer.writerows(json_import)


def csv_to_json(csv_path: str, json_path: str) -> None:
    json_path = Path(json_path)
    csv_path = Path(csv_path)

    if csv_path.exists() == False:
        raise FileNotFoundError

    if len(csv_path.read_text(encoding="utf-8")) <= 0:
        raise ValueError

    list_line_csv = []

    with csv_path.open('r', encoding='utf-8') as f:
        csv_read = csv.DictReader(f)
        for line in csv_read:
            list_line_csv.append(line)

    with json_path.open("w", newline='', encoding="utf-8") as f:
        json_writer = json.dump(list_line_csv, f, ensure_ascii=False, indent=2)

    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """

json_to_csv("/Users/grom61/PycharmProjects/python_labs/data/samples/people.json",'/Users/grom61/PycharmProjects/python_labs/data/out/people_from_json.csv')
csv_to_json("/Users/grom61/PycharmProjects/python_labs/data/samples/people.csv",'/Users/grom61/PycharmProjects/python_labs/data/out/people_from_csv.json')