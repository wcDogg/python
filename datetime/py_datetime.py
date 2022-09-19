import datetime
import time
import pytz

# ------------------------------------
# `datetime.datetime(y,m,d,hr,min,sec,ms,tmz)`
# Naive by default. Can be made aware.
# ------------------------------------

year = 2022
month = 12
day = 31
hr = 23
min = 59
sec = 59
mic = 999999

# Integers to datetime
# > 2022-12-31 23:59:59.999999
dt_01 = datetime.datetime(year,month,day,hr,min,sec,mic)
print(f'Integers to DT: {dt_01}')

# String to datetime
# '%m-%d-%Y' is the INPUT format - NOT output.
# > 2022-12-31 00:00:00
date_string = '12-31-2022'
date_02 = datetime.datetime.strptime(date_string, '%m-%d-%Y')
print(f'String to DT: {date_02}')

# Datetime to string
# Format describes INPUT - not output
# > 2022-12-31 23:59:59.999999
dt_string  = datetime.datetime.strftime(dt_01, "%Y-%m-%d %H:%M:%S.%f")
print(f'DT to String: {dt_string}')

# Datetime to ISO
# > 2022-12-31T23:59:59.999999
dt_iso = dt_01.isoformat()
print(f'DT ISO: {dt_iso}')

# ------------------------------------
# Current local datetime 
# ------------------------------------

# `.tocay()` - no timezone
# > 2022-03-01 00:54:09.550928
dt_today = datetime.datetime.today()
print(f'DT Today: {dt_today}')

# `.now()` - can pass in tmz
# > 2022-03-01 00:54:09.550928
dt_now = datetime.datetime.now()
print(f'DT Now: {dt_now}')

# `.utcnow()` - can pass in tmz
# > 2022-03-01 05:54:09.550928
dt_utcnow = datetime.datetime.utcnow()
print(f'DT UTC Now: {dt_utcnow}')

# ------------------------------------
# Timezones 
# ------------------------------------

# Timezone aware datetime usint pytmz
# > 2016-12-25 23:59:00+00:00
tz_dt = datetime.datetime(2016,12,25,23,59,tzinfo=pytz.UTC)
print(f'DT with TMZ: {tz_dt}')

# Now time with timezone
# > 2022-03-01 20:02:15.713392+00:00
tz_now = datetime.datetime.now(tz=pytz.UTC)
print(f'DT Now + TMZ: {tz_now}')

# Now UTC with timezone
# Same result as above, but awkward
# > 2022-03-01 20:02:15.713392+00:00
tz_utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(f'DT UTC Now + TMZ: {tz_utc_now}')

# Convert to a different timezone
eastern = pytz.timezone('US/Eastern')
mountain = pytz.timezone('US/Mountain')

print(f'Timezone Eastern: {eastern}')
print(f'Timezone Mountain: {mountain}')

dt_est = tz_utc_now.astimezone(eastern)
print(f'UTC to Eastern: {dt_est}')

dt_mount = tz_utc_now.astimezone(mountain)
print(f'UTC to Mountain: {dt_mount}')

# Naive date to datetime with tmz
n_date = datetime.datetime.now()
print(f'Naive Now: {n_date}')
n_date = eastern.localize(n_date)
print(f'Naive to Awaare: {n_date}')

# Print pytz timezone names
def pytz_tz_names():
  for tz in pytz.all_timezones:
    print(f'{tz}')

# pytz_tz_names()


# ------------------------------------
# Extracting from datetime
# ------------------------------------

# print(f'DT Date: {dt_01.date()}')
# print(f'DT Time: {dt_01.time()}')
# print(f'DT Year: {dt_01.year}')
# print(f'DT Month: {dt_01.month}')
# print(f'DT Day: {dt_01.day}')
# print(f'DT Hour: {dt_01.hour}')
# print(f'DT Minute: {dt_01.minute}')
# print(f'DT Second: {dt_01.second}')
# print(f'DT Micro: {dt_01.microsecond}')


# ------------------------------------
# `datetime.timedelta()`
# Adding and subtracting datetimes
# new_tdelta = dt_01 + dt_02
# new_time = dt + timedelta
# ------------------------------------

# Duration - adding and subtracting
# > 2022-01-01 : 7 :  2022-01-08
duration = datetime.timedelta(days=7)
end_date = dt_01.date() + duration
print(f'DT Duration: {dt_01.date()} : {duration.days} : {end_date}')


