from datetime import date
today = date.today()
my_birthday = date(today.year, 4, 8)
if my_birthday < today:
    my_birthday = my_birthday.replace(year=today.year + 1)
time_to_birthday = abs(my_birthday - today)

print(time_to_birthday.days)
