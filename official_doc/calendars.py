import calendar

# Checking if a Year is a Leap Year
is_leap = calendar.isleap(2024)  # True for leap year
print(is_leap)

# Getting the Last Day of a Month
year, month = 2024, 2
last_day = calendar.monthrange(year, month)[1]
print(f"Last day of {year}-{month} is {last_day}")

# Calculating the Number of Days in a Month
num_days = calendar.monthrange(2024, 2)[1]
print(f"Number of days in February 2024: {num_days}")