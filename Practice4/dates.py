import datetime

now = datetime.datetime.now()
print("Сейчас:", now)

print("Сегодня:", now.strftime("%d-%m-%Y"))

birthday = datetime.date(2026, 9, 22)
days_left = birthday - now.date()
print("До дня рождения осталось:", days_left.days, "дней")

