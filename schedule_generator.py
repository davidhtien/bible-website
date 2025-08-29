import pythonbible as pb
from datetime import datetime as dt
from datetime import timedelta as td

import json

start_date = dt(2025, 9, 1, 9, 0, 0)

schedule = []

for book in pb.BOOK_GROUPS["New Testament"]:
    n = pb.get_number_of_chapters(book)
    for i in range(1, n + 1):
        formatted = start_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        reading = book.title + " " + str(i)
        day_chapter = {"date": formatted, "reading": reading}

        schedule.append(day_chapter)

        start_date = start_date + td(days=1)


schedule_json = json.dumps(schedule)
print(schedule_json)