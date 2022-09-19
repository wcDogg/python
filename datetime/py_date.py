import datetime

# ------------------------------------
# `datetime.date(year,month,day)`
# Always naive
# ------------------------------------

# Integer to date
# > 2022-12-31
y,m,d = 2022,12,31
date_01 = datetime.date(y,m,d)
print(f'Integers to Date: {date_01}')

# String to date
# '%m-%d-%Y' is the INPUT format - NOT output.
# > 2022-12-31
date_string = '12-31-2022'
date_02 = datetime.datetime.strptime(date_string, '%m-%d-%Y').date()
print(f'String to Date: {date_02}')

# Date to ISO
date_iso = date_02.isoformat()
print(f'Date to ISO: {date_iso}')

# Date to ISO tuple
# > datetime.IsoCalendarDate(year=2022, week=52, weekday=6)
date_iso_tuple = date_02.isocalendar()
print(f'Date ISO Tuple: {date_iso_tuple}')
print(f'ISO Year: {date_iso_tuple.year}')
print(f'ISO Week: {date_iso_tuple.week}')
print(f'ISO Weekday: {date_iso_tuple.weekday}')

# ISO day of week
# [1] Monday to [7] Sunday
iso_dow = date_02.isoweekday()
print(f'ISO Weekday: {iso_dow}')

# Machine day of week
# [0] Monday to [6] Sunday
machine_dow = date_02.weekday()
print(f'Machine Weekday: {machine_dow}')

# Current local date (no tmz)
today = datetime.date.today()
print(f'Today: {today}')

# Extracting integers from date
print(f'Today Year: {today.year}')
print(f'Today Month: {today.month}')
print(f'Today Day: {today.day}')

# ------------------------------------
# `datetime.timedelta()`
# Adding and subtracting dates
# new_tdelta = date_01 + date_02
# new_date = date + timedelta
# ------------------------------------

# Duration - adding and subtracting
# > 2022-01-01 / 7 /  2022-01-08
start_date = datetime.date(2022,1,1)
duration = datetime.timedelta(days=7)
end_date = start_date + duration
print(f'Duration: {start_date} : {duration.days} : {end_date}')

# How old am I?
today = datetime.date.today()
purchased = datetime.date(2011,12,25)
age = today - purchased

# Extracting from timedelta
# > 3716 days, 0:00:00
print(f'Age TD: {age}')
# > 3167
print(f'Age TD Days: {age.days}')
# > 321062400.0
print(f'Age TD Secs: {age.total_seconds()}')

# Converting to years, months days
# result_years = None
# print(f'Years: {result_years}')

# result_months = None
# print(f'Months: {result_months}')

# result_days = None
# print(f'Days: {result_days}')

