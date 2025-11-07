import argparse
from functions import read_files
from reports import form_report, REPORTS_NAMES

def main():
    parser = argparse.ArgumentParser(description="Обработка CSV файлов")
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Список CSV-файлов"
    )
    parser.add_argument(
        "--report",
        choices=REPORTS_NAMES,
        required=True,
        help="Тип отчёта"
    )

    args = parser.parse_args()
    data = read_files(args.files)
    form_report(data, args.report)

if __name__ == "__main__":
    main()
