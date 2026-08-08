import datetime
import time

print("=" * 60)
print("Handling Numbers, Dates and Time")
print("=" * 60)

currentDT = datetime.datetime.now()

print("\nCurrent Date and Time Information\n")

print("Current Year         :", currentDT.year)
print("Current Month        :", currentDT.month)
print("Current Day          :", currentDT.day)
print("Current Hour         :", currentDT.hour)
print("Current Minute       :", currentDT.minute)
print("Current Second       :", currentDT.second)
print("Current Microsecond  :", currentDT.microsecond)
print("Current Date         :", currentDT.date())
print("Current Time         :", currentDT.time())
print("Current DateTime     :", currentDT)
print("After 365 Days       :", currentDT + datetime.timedelta(days=365))
print("Timezone Info        :", currentDT.tzinfo)

print("\n" + "=" * 60)
print("Time Module Functions")
print("=" * 60)

# Current timestamp
print("time.time()              :", time.time())

# Local time
print("time.localtime()         :", time.localtime())

# GMT / UTC time
print("time.gmtime()            :", time.gmtime())

# Convert to readable string
print("time.ctime()             :", time.ctime())

# Formatted local time
print("time.asctime()           :", time.asctime())

# Formatted date/time
print("time.strftime()          :", time.strftime("%d-%m-%Y %H:%M:%S"))

# Parse string to struct_time
print("time.strptime()          :",
      time.strptime("01 Aug 2026", "%d %b %Y"))

# Timezone
print("time.timezone            :", time.timezone)

# Alternate timezone
print("time.altzone             :", time.altzone)

# Daylight Saving Time
print("time.daylight            :", time.daylight)

# Timezone names
print("time.tzname              :", time.tzname)

# High resolution timer
print("time.perf_counter()      :", time.perf_counter())

# CPU processing time
print("time.process_time()      :", time.process_time())

# Monotonic clock
print("time.monotonic()         :", time.monotonic())

# Nanosecond timestamp
print("time.time_ns()           :", time.time_ns())

# Nanosecond performance counter
print("time.perf_counter_ns()   :", time.perf_counter_ns())

# Nanosecond monotonic clock
print("time.monotonic_ns()      :", time.monotonic_ns())

# Process time in nanoseconds
print("time.process_time_ns()   :", time.process_time_ns())

# Clock information
print("\nClock Information")
print("time.get_clock_info('time')         :", time.get_clock_info('time'))
print("time.get_clock_info('perf_counter') :", time.get_clock_info('perf_counter'))
print("time.get_clock_info('monotonic')    :", time.get_clock_info('monotonic'))
print("time.get_clock_info('process_time') :", time.get_clock_info('process_time'))

# Sleep demonstration
print("\nSleeping for 2 seconds...")
time.sleep(2)
print("Done!")
import calendar 
print(calendar.calendar(2026, w=3, l=1, c=4))
print(calendar.isleap(2004))
print(calendar.month(2026, 8, w=3, l=1))
print(calendar.weekday(2026, 8, 1))
print(calendar.timegm([2026, 8, 1, 0, 0, 0]))