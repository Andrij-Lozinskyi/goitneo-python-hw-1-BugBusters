from collections import defaultdict
from datetime import datetime, timedelta
import calendar

def get_birthdays_per_week(users):
    birthdays_per_week = defaultdict(list)
    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days 

        if delta_days < 7: 
            weekdays = list(calendar.day_name)
            weekday_number = birthday_this_year.weekday()
            if weekday_number == 5 or weekday_number == 6:
                day_of_week = "Monday"
            else: 
                day_of_week = weekdays[weekday_number]
            birthdays_per_week[day_of_week].append(name)

    for day, names in birthdays_per_week.items():
        print(f"{day}: {', '.join(names)}")

users = [
    {"name": "Ben Franklin", "birthday": datetime(1945, 12, 11)},
    {"name": "Stephen King", "birthday": datetime(1945, 12, 12)},
    {"name": "Georgy Baloon", "birthday": datetime(1945, 12, 13)},
    {"name": "Hannibal Lecter", "birthday": datetime(1945, 12, 14)},
    {"name": "Abraham Lincoln", "birthday": datetime(1945, 12, 15)},
    {"name": "Jack Sparrow", "birthday": datetime(1945, 12, 16)},
    {"name": "Captain Zorg", "birthday": datetime(1945, 12, 17)},
    {"name": "Johny Storm", "birthday": datetime(1945, 12, 30)}
]

get_birthdays_per_week(users)