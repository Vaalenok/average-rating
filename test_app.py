import sys
from main import main
from functions import read_files
from reports import average_rating, form_report, REPORTS_NAMES

def test_read_files_valid(tmp_path):
    csv_file = tmp_path / "products.csv"
    csv_file.write_text("name,brand,price,rating\niphone,apple,999,4.9\n")
    data = read_files([str(csv_file)])
    assert data == [{'name': 'iphone', 'brand': 'apple', 'price': '999', 'rating': '4.9'}]

def test_read_files_invalid_file(tmp_path, capsys):
    invalid_file = tmp_path / "invalid.txt"
    invalid_file.write_text("not a csv")
    data = read_files([str(invalid_file)])
    captured = capsys.readouterr()
    assert "не является CSV" in captured.out
    assert data == []

def test_read_files_nonexistent(tmp_path, capsys):
    data = read_files([str(tmp_path / "nofile.csv")])
    captured = capsys.readouterr()
    assert "не найден" in captured.out
    assert data == []

def test_average_rating():
    data = [
        {"name": "iphone", "brand": "apple", "price": "999", "rating": "4.9"},
        {"name": "iphone 2", "brand": "apple", "price": "1099", "rating": "4.7"},
        {"name": "galaxy", "brand": "samsung", "price": "1199", "rating": "4.8"}
    ]

    headers, result = average_rating(data)
    assert headers == ["#", "brand", "rating"]
    assert result[0][1] == "apple"
    assert result[0][2] == round((4.9+4.7)/2,2)
    assert result[1][1] == "samsung"

def test_average_rating_with_invalid_rating():
    data = [{"name": "iphone", "brand": "apple", "price": "999", "rating": "wefsd"}]
    headers, result = average_rating(data)
    assert result == []

def test_form_report_print(capsys):
    data = [
        {"name": "iphone", "brand": "apple", "price": "999", "rating": "4.9"}
    ]
    form_report(data, "average-rating")
    captured = capsys.readouterr()
    assert "apple" in captured.out

def test_form_report_invalid_name(capsys):
    form_report([], "nonexistent-report")
    captured = capsys.readouterr()
    assert "Ошибка" in captured.out

def test_reports_names():
    assert "average-rating" in REPORTS_NAMES

def test_main_cli(monkeypatch, tmp_path):
    csv_file = tmp_path / "products.csv"
    csv_file.write_text("name,brand,price,rating\niphone,apple,999,4.9\n")
    monkeypatch.setattr(sys, "argv", ["main.py", "--files", str(csv_file), "--report", "average-rating"])
    main()
