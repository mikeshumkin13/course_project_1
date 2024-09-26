import pandas as pd
import json
from datetime import datetime


def generate_report(file_path):
    # Чтение данных из Excel
    df = pd.read_excel(file_path)

    # Пример обработки данных: подсчет суммы операций по категориям
    report = df.groupby("Категория")["Сумма операции"].sum().reset_index()

    # Сохранение отчета в формате JSON
    report_json = report.to_json(orient="records")
    with open("report.json", "w") as f:
        f.write(report_json)

    return report
