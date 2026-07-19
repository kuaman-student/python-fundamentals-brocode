import datetime

x = datetime.datetime.now()
print(x)

date = datetime.date(2026, 7, 19)
print(date)
print(datetime.date.today())
time = datetime.time(10, 36)
print(time)

# Python strftime() Format Codes
# YEAR
# %Y -> Year with century (4 digits)
#       Example: 2026
# %y -> Year without century (2 digits, zero-padded)
#       Example: 26

# MONTH
# %m -> Month as a zero-padded number (01-12)
#       Example: 07
# %B -> Full month name
#       Example: July
# %b -> Abbreviated month name
#       Example: Jul
#
# DAY
# %d -> Day of the month (01-31)
#       Example: 19
# %A -> Full weekday name
#       Example: Sunday
# %a -> Abbreviated weekday name
#       Example: Sun
#
# TIME
# %H -> Hour (24-hour format, 00-23)
#       Example: 13
# %I -> Hour (12-hour format, 01-12)
#       Example: 01
# %p -> AM / PM
#       Example: PM
# %M -> Minute (00-59)
#       Example: 45
# %S -> Second (00-59)
#       Example: 30
# %f -> Microsecond (000000-999999)
#       Example: 123456
#
# COMMON COMBINATIONS
# %d/%m/%Y           -> 19/07/2026
# %d-%m-%Y           -> 19-07-2026
# %Y-%m-%d           -> 2026-07-19
# %B %d, %Y          -> July 19, 2026
# %A, %d %B %Y       -> Sunday, 19 July 2026
# %H:%M:%S           -> 13:45:30
# %I:%M:%S %p        -> 01:45:30 PM
# %d/%m/%Y %H:%M:%S  -> 19/07/2026 13:45:30

print(x.strftime("%d/%m/%Y"))
print(x.strftime("%H:%M:%S"))