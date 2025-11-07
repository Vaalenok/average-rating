import tabulate
from collections import defaultdict

REPORTS_NAMES = ["average-rating"]

def form_report(data, report_name):
    headers, result = None, None

    match report_name:
        case "average-rating":
            headers, result = average_rating(data)

    if not result:
        print("Ошибка: Не удалось создать отчёт")
        return

    print(tabulate.tabulate(result, headers=headers, tablefmt="grid"))

def average_rating(data):
    grouped_ratings = defaultdict(list)

    for product in data:
        brand = product.get("brand")

        try:
            rating = float(product.get("rating"))
            grouped_ratings[brand].append(rating)
        except (ValueError, TypeError):
            continue

    avg_ratings_list = []

    for brand, ratings in grouped_ratings.items():
        if ratings:
            avg = round(sum(ratings) / len(ratings), 2)
            avg_ratings_list.append([brand, avg])
        else:
            avg_ratings_list.append([brand, None])

    avg_ratings_list.sort(key=lambda x: x[1], reverse=True)
    data_with_index = [[i + 1] + row for i, row in enumerate(avg_ratings_list)]

    return ["#", "brand", "rating"], data_with_index
