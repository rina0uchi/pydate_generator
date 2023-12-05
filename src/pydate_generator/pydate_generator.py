from datetime import date, timedelta

# Generate dates one by one in order from start to end.
# timedelta(1) = 1 day, 0:00:00
def gen_dates(start, end):
    end += timedelta(1)
    step = timedelta(1)
    current = start
    while current < end:
        yield current
        current += step


if __name__ == '__main__':
    print("Enter start date. (e.g. 2023-12-23)")
    nums = list(map(int, input().split("-")))
    start = date(nums[0], nums[1], nums[2])

    print("Enter end date. (e.g. 2024-1-3)")
    nums = list(map(int, input().split("-")))
    end = date(nums[0], nums[1], nums[2])
    print("")

    for date in gen_dates(start, end):
        print(date)