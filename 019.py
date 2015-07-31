from datetime import date, timedelta

def daterange(start, end):
    for n in range(int((end - start).days)):
        yield start + timedelta(n)

is_first_and_sunday = lambda date: date.day == 1 and date.weekday() == 6

print(len(list(filter(is_first_and_sunday, daterange(date(1901, 1, 1), date(2000, 12, 31))))))
