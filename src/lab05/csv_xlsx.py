import openpyxl
from pathlib import Path
import csv


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    csv_path = Path(csv_path)
    xlsx_path = Path(xlsx_path)

    if csv_path.exists() == False:
        raise FileNotFoundError

    if len(csv_path.read_text(encoding="utf-8")) <= 0:
        return ""

    xlsx_book = openpyxl.Workbook()
    xlsx_sheet1 = xlsx_book.active
    xlsx_sheet1.title = "Sheet1"

    with csv_path.open('r', encoding='utf-8') as f:
        csv_read = csv.reader(f)

        for row in csv_read:
            xlsx_sheet1.append(row)

    xlsx_book.save(xlsx_path)


csv_to_xlsx("/Users/grom61/PycharmProjects/python_labs/data/samples/people.csv", "/Users/grom61/PycharmProjects/python_labs/data/out/people.xlsx")



