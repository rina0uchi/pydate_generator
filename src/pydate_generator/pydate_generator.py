from datetime import date, timedelta

# Generate dates one by one in order from start to end.
# timedelta(1) = 1 day, 0:00:00
def date_generator(start, end):
    end += timedelta(1)
    step = timedelta(1)
    current = start
    while current < end:
        yield current
        current += step


if __name__ == '__main__':
    start = date(2023, 12, 23)
    end = date(2024, 1, 5)
    
    for date in date_generator(start, end):
        print(date)