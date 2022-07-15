import datetime
import time
import pytz

# ------------------------------------
# `datetime.time(hr,min,sec,ms, tmz)`
# Naive by default. Can be made aware.
# ------------------------------------

h, m, s, ms = 9,38,45,100000

# Inegers to time
# > 09:38:45.100000
naive_time = datetime.time(h,m,s,ms)
print(f'Integers to Time: {naive_time}')

# String to time
# > 

# Time to ISO
# > 

# Current naive local time
# > 
dt_local = time.localtime()
print(f'Local Time: {dt_local}')

# Local time to string
# Format describes INPUT - not output.
# > 2022-02-27 17:32:51
dt_local_string  = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(f'Local Time to String: {dt_local_string}')

# Extracting integers from time
print(f'Time Hours: {naive_time.hour}')
print(f'Time Minutes: {naive_time.minute}')
print(f'Time Seconds: {naive_time.second}')
print(f'Time Micro: {naive_time.microsecond}')



