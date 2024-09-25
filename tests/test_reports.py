import pytest
import pandas as pd
from src.reports import generate_report

def test_generate_report():
    report = generate_report('data/operations.xlsx')
    assert isinstance(report, pd.DataFrame)  # Проверяем, что результат — это DataFrame
    assert not report.empty  # Проверяем, что отчет не пустой