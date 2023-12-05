# pydate_generator
Given a start and end date, this generator returns a sequence of dates that includes the start and end dates.
開始日と終了日を指定すると，開始日と終了日を含む日付を順に返すジェネレーターです．


# Installation
Download this repogitory and use pip.
```
pip install pydate_generator/
```

# Example
```python
from datetime import date
import pydate_generator

start = date(2023, 12, 23)
end = date(2024, 1, 5)

for date in pydate_generator.gen_dates(start, end):
    print(date)
```
Output
```terminal
2023-12-23
2023-12-24
2023-12-25
2023-12-26
2023-12-27
2023-12-28
2023-12-29
2023-12-30
2023-12-31
2024-01-01
2024-01-02
2024-01-03
2024-01-04
2024-01-05
```

# Lisence
This project is licensed under the MIT License, see the LICENSE file for details.