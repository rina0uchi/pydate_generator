from datetime import date
import pydate_generator


def test_gen_dates():

    start = date(2023, 12, 23)
    end = date(2024, 1, 5)

    outputs = [str(date) for date in pydate_generator.gen_dates(start, end)]
    expects = [
        "2023-12-23",
        "2023-12-24",
        "2023-12-25",
        "2023-12-26",
        "2023-12-27",
        "2023-12-28",
        "2023-12-29",
        "2023-12-30",
        "2023-12-31",
        "2024-01-01",
        "2024-01-02",
        "2024-01-03",
        "2024-01-04",
        "2024-01-05"
    ]
    for expect, output in zip(expects, outputs):
        assert expect == output