import requests
from bs4 import BeautifulSoup
from cachetools import TTLCache
import os

# Файл с группами
GROUPS_FILE = os.path.join(os.path.dirname(__file__), "groups.txt")

# Кеш с тайм-аутом 300 секунд (5 минут) и максимумом на 100 записей
cache = TTLCache(maxsize=100, ttl=300)


def load_groups():
    """Читает файл groups.txt и возвращает словарь групп и их ID."""
    groups = {}
    with open(GROUPS_FILE, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line and ":" in line:
                group_name, group_id = line.split(":", 1)
                groups[group_name.strip()] = group_id.strip()
    return groups


GROUPS = load_groups()


def get_group_id_by_name(group_name):
    """Получение ID группы по названию."""
    return GROUPS.get(group_name)


def get_schedule_from_cist(group_id, start_date, end_date):
    """Получение расписания с CIST с кешированием."""
    cache_key = f"{group_id}_{start_date}_{end_date}"

    # Если запрос уже был выполнен и есть в кеше, возвращаем кешированный результат
    if cache_key in cache:
        print("Возвращаем данные из кеша")
        return cache[cache_key]

    base_url = "https://cist.nure.ua/ias/app/tt/f"
    params = {
        "p": f"778:201:2687770147176185:::201:P201_FIRST_DATE,P201_LAST_DATE,P201_GROUP,P201_POTOK:{start_date},{end_date},{group_id},0"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        schedule_table = soup.find("table", class_="MainTT")

        if not schedule_table:
            return {"error": "Расписание не найдено: таблица отсутствует"}

        rows = schedule_table.find_all("tr")
        schedule = {week: {} for week in range(1, 25)}
        day = None

        for row in rows:
            cells = row.find_all("td")

            if len(cells) > 1 and "date" in cells[0].get("class", []):
                day = cells[0].text.strip()

            elif len(cells) > 2 and day is not None:
                time = cells[1].text.strip()

                for week_index, cell in enumerate(cells[2:], start=1):
                    lesson = cell.text.strip()
                    if lesson:
                        lesson_type = ""
                        if "Лк" in lesson:
                            lesson_type = "Лекція"
                        elif "Пз" in lesson:
                            lesson_type = "Практика"
                        elif "Лб" in lesson:
                            lesson_type = "Лабораторна"
                        elif "Зал" in lesson:
                            lesson_type = "Залік"
                        elif "Ісп" in lesson:
                            lesson_type = "Іспит"
                        elif "Конс" in lesson:
                            lesson_type = "Консультація"

                        if day not in schedule[week_index]:
                            schedule[week_index][day] = []
                        schedule[week_index][day].append(
                            {"time": time, "lesson": lesson, "type": lesson_type}
                        )

        # Сохраняем полученные данные в кеш
        cache[cache_key] = schedule
        print("Данные добавлены в кеш")
        return schedule
    else:
        return {"error": f"Ошибка запроса: {response.status_code}"}
