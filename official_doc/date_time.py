from datetime import datetime, date, time, timedelta, timezone
import pytz
# from dateutil import parser
# import pandas as pd

# Getting Current Date and Time
now = datetime.now()  # Current local date and time
utc_now = datetime.utcnow()  # Current UTC date and time
today = date.today()  # Current date only
print(now, utc_now, today)

# Getting Date and Time Components
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
weekday = now.weekday()  # Monday is 0, Sunday is 6
d = now.date()
t = now.time()

print(year, month, day, hour, minute, second, weekday, d, t)

# Creating a datetime object
dt = datetime(2024, 11, 11, 15, 30, 45)
print(dt)  # 2024-11-11 15:30:45

# Creating a date object
d = date(2024, 11, 11)
print(d)  # 2024-11-11

# Creating a time object
t = time(15, 30, 45)
print(t)  # 15:30:45

# Parsing datetime from a string
dt_str = "2024-11-11 15:30:45"
dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
t = dt.time()
# Alternatively, using `dateutil.parser`
# dt_alt = parser.parse(dt_str)
print('Parsing datetime from a string:')
print(dt)
print(t)

# Formatting datetime to a string
formatted_str = dt.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_str)  # 2024-11-11 15:30:45

# Date Arithmetic with timedelta
# Adding days
future_date = now + timedelta(days=10)

# Subtracting days
past_date = now - timedelta(days=10)

# Difference between two dates
diff = future_date - past_date
print(diff.days, diff.total_seconds())

# Converting datetime to UNIX Timestamp
timestamp = now.timestamp()
print(timestamp)

# Converting UNIX Timestamp back to datetime
dt_from_timestamp = datetime.fromtimestamp(timestamp)
print(dt_from_timestamp)

# Replacing Date or Time Components
new_dt = now.replace(year=2025, month=12, day=25, hour=10)
print(new_dt)  # Modified datetime

# Rounding a datetime
def round_to_minute(dt):
    return dt.replace(second=0, microsecond=0)

rounded_dt = round_to_minute(now)
print(rounded_dt)

# Getting the Start of the Day (midnight)
start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
print(start_of_day)

# Getting Week Number of the Year
week_number = now.isocalendar().week
print(week_number)

# Calculating Age from a Birth Date
birth_date = date(1989, 8, 10)
age = (today - birth_date).days // 365
print(f"Age: {age} years")

# ISO Format Conversion
# Convert to ISO format string
iso_str = now.isoformat()
print(iso_str)

# Parse ISO format string
dt_from_iso = datetime.fromisoformat(iso_str)
print(dt_from_iso)

# Iterating Through a Date Range
start_date = date(2024, 1, 1)
end_date = date(2024, 1, 10)

current_date = start_date
while current_date <= end_date:
    print(current_date)
    current_date += timedelta(days=1)

# Getting Day of the Week
day_of_week = now.strftime("%A")  # Full weekday name
print(day_of_week)

# Date Validation
def is_valid_date(year, month, day):
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

print(is_valid_date(2024, 2, 30))  # False (Feb 30 does not exist)

#TimeZone 

# Get current UTC datetime
utc_now = datetime.utcnow()
print(utc_now)

# Get current UTC datetime with timezone info
utc_now = datetime.now(timezone.utc)
print(utc_now)
print(utc_now.isoformat())  # Outputs: '2024-11-11T14:35:00.000Z'

# Convert to ISO 8601 with timezone offset
utc_now = datetime.now(timezone.utc)
local_time = utc_now.astimezone()
print(local_time)
print(local_time.isoformat())  # Outputs: '2024-11-11T19:05:00+05:30' (for IST)

# Get current UTC datetime using pytz
utc_now = datetime.now(pytz.utc)
print(utc_now)

# Time Zone Handling with pytz
tz = pytz.timezone('America/New_York')
dt_with_tz = tz.localize(now)

# Converting to another timezone
dt_utc = dt_with_tz.astimezone(pytz.utc)
print('Handling Timezones:')
print(dt_with_tz, dt_utc)

# Date Range Generation
# date_range = pd.date_range(start="2024-01-01", end="2024-01-10")
# print(date_range)