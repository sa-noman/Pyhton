"""Dates and times."""
from datetime import date, datetime, timedelta
today = date.today()
now = datetime.now()
tomorrow = today + timedelta(days=1)
print(today)
print(now.strftime("%Y-%m-%d %H:%M"))
print(tomorrow)
