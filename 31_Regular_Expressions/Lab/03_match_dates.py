import re

recieve_dates = input()
regex = (r"\d{2}/(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"
         r"/\d{4}|\d{1,2}-(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"
         r"-\d{4}|\d{1,2}\.(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\.\d{4}")

find_dates = re.findall(regex, recieve_dates)

for date in find_dates:
    if '/' in date:
        day, month, year = date.split('/')
    elif '-' in date:
        day, month, year = date.split('-')
    else:
        day, month, year = date.split('.')
    print(f"Day: {day}, Month: {month}, Year: {year}")
