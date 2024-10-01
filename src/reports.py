import json
import pandas as pd


def generate_report(file_path):
    """Генерирует отчет по категориям расходов и сохраняет его в JSON."""
    # Чтение данных из Excel
    df = pd.read_excel(file_path)

    # Подсчет суммы операций по категориям
    report = df.groupby("Категория")["Сумма операции"].sum().reset_index()

    # Сохранение отчета в формате JSON
    report_json = report.to_json(orient="records", ensure_ascii=False)
    report_file_path = "report.json"
    with open(report_file_path, "w", encoding='utf-8') as f:
        f.write(report_json)

    return report