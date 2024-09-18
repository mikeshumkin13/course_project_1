from reports import generate_report

if __name__ == "__main__":
    file_path = 'data/operations.xlsx'
    report = generate_report(file_path)
    print(report)