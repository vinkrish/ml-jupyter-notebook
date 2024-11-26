from dateutil.parser import parse
from datetime import datetime
import pytz

# Basic Date Parsing
date = parse("2024-11-13")
print(date)  # Output: 2024-11-13 00:00:00

# Parsing Date and Time
date = parse("2024-11-13 15:30:45")
print(date)  # Output: 2024-11-13 15:30:45

# Parsing Different Date Formats
date1 = parse("13th November, 2024")
date2 = parse("11/13/2024")
date3 = parse("13-Nov-2024")

print(date1)  # Output: 2024-11-13 00:00:00
print(date2)  # Output: 2024-11-13 00:00:00
print(date3)  # Output: 2024-11-13 00:00:00

# Parsing with Time Zone Information
date = parse("2024-11-13T15:30:45+05:30")
print(date)  # Output: 2024-11-13 15:30:45+05:30

# Ignoring Time Zone Information (ignoretz=True)
date = parse("2024-11-13T15:30:45+05:30", ignoretz=True)
print(date)  # Output: 2024-11-13 15:30:45

# Handling Ambiguous Dates (Day First)
date = parse("13/11/2024", dayfirst=True)
print(date)  # Output: 2024-11-13 00:00:00

# Handling Fuzzy Strings
date = parse("The event is on 2024-11-13 at 10 AM", fuzzy=True)
print(date)  # Output: 2024-11-13 10:00:00

# Handling ISO date
date = parse("2024-11-13T15:30:45Z")
print(date)  # Output: 2024-11-13 15:30:45+00:00

# Parsing Dates with Missing Components
date = parse("November 2024")
print(date)  # Output: 2024-11-01 00:00:00

# Custom Default Values
default = datetime(2024, 11, 13, 12, 0, 0)
date = parse("November", default=default)
print(date)  # Output: 2024-11-13 12:00:00

# Error Handling
try:
    date = parse("invalid date")
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Unknown string format: invalid date

# Parsing Time Only
time = parse("15:45").time()
print(time)  # Output: 15:45:00

# Parsing Dates with Different Separators
date = parse("2024.11.13")
print(date)  # Output: 2024-11-13 00:00:00

#----------pytz----------
now = datetime.now()

# Time Zone Handling with pytz
tz = pytz.timezone('America/New_York')
dt_with_tz = tz.localize(now)

# Converting to another timezone
dt_utc = dt_with_tz.astimezone(pytz.utc)
print(dt_with_tz, dt_utc)

timezone = pytz.timezone("America/New_York")
current_time = datetime.now(timezone)
print(current_time)  # Output: 2024-11-13 10:45:32.123456-05:00

# Convert a Naive datetime to a Time Zone
timezone = pytz.timezone("Europe/London")
naive_dt = datetime(2024, 11, 13, 15, 30)
localized_dt = timezone.localize(naive_dt)
print(localized_dt)  # Output: 2024-11-13 15:30:00+00:00

# Convert Between Time Zones
timezone_ny = pytz.timezone("America/New_York")
timezone_sf = pytz.timezone("America/Los_Angeles")

ny_time = timezone_ny.localize(datetime(2024, 11, 13, 12, 0))
sf_time = ny_time.astimezone(timezone_sf)
print(sf_time)  # Output: 2024-11-13 09:00:00-08:00

# Handling Daylight Saving Time (DST)
timezone = pytz.timezone("America/New_York")

# During standard time
dt_standard = timezone.localize(datetime(2024, 1, 13, 12, 0))
print(dt_standard.tzname())  # Output: EST

# During daylight saving time
dt_dst = timezone.localize(datetime(2024, 7, 13, 12, 0))
print(dt_dst.tzname())  # Output: EDT

# Get the Time Zone Name and Offset
timezone = pytz.timezone("Asia/Kolkata")
localized_dt = timezone.localize(datetime(2024, 11, 13, 15, 30))
print(localized_dt.tzname())  # Output: IST
print(localized_dt.utcoffset())  # Output: 5:30:00

# UTC Conversion
utc_time = datetime.utcnow().replace(tzinfo=pytz.UTC)
print(utc_time)  # Output: 2024-11-13 14:45:32.123456+00:00

ny_time = timezone_ny.localize(datetime(2024, 11, 13, 12, 0))
utc_time = ny_time.astimezone(pytz.UTC)
print(utc_time)  # Output: 2024-11-13 17:00:00+00:00

# Convert a UTC datetime to a Local Time Zone
utc_dt = pytz.UTC.localize(datetime(2024, 11, 13, 14, 0))
local_tz = pytz.timezone("Asia/Tokyo")
local_dt = utc_dt.astimezone(local_tz)
print(local_dt)  # Output: 2024-11-13 23:00:00+09:00

# Convert ISO 8601 String to Time Zone Aware datetime
iso_str = "2024-11-13T15:30:00Z"
aware_dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
print(aware_dt)  # Output: 2024-11-13 15:30:00+00:00
