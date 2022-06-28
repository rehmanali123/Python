import datetime


d = datetime.date(2021, 7, 3)
print(d)

# current local date
today = datetime.date.today()
print(today) 

print("Today's year is: ", today.year)
print("Today's day is: ", today.day)
print("Today's day of the week is: ", today.weekday())      # monday = 0, sunday = 6
print("Today's day of the week is: ", today.isoweekday())   # monday = 1, sunday = 7

# time delta

time_delta = datetime.timedelta(days=21)

print("21 days after, date will be: ", today + time_delta)
print("21 days before, date was: ", today - time_delta)

# Time until Birthday

birthday = datetime.date(2022, 8, 23)

till_date = birthday - today
print(till_date.days)
print(till_date.total_seconds())


# time
time = datetime.time(9, 30, 9, 100000)
print(time)


# current local datetime 
dt = datetime.datetime.now()
print(dt.date())
print(dt.time())

# return current local date time with timezone = none
dt_today = datetime.datetime.today()

# we can pass time zone info 
dt_now = datetime.datetime.now()

# still not timezone aware... just utc now
dt_utcnow = datetime.datetime.utcnow()

print("Today is: ", dt_today)
print("Now is: ", dt_now)
print("UTC Now is: ", dt_utcnow)

# using Time Zones

import pytz

dt = datetime.datetime(2022, 9,3, 9,30,35, tzinfo = pytz.UTC)
dt_now = datetime.datetime.now(tz=pytz.UTC)
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

print(dt)
print("Current UTC time: ", dt_now)
print("Current UTC time: ", dt_utcnow)


# UTC DateTime ... timezone aware
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)


# convert it to local timezone
date_mtn = dt_utcnow.astimezone(pytz.timezone('Asia/Karachi'))
print(date_mtn)

# naive date time
dt = datetime.datetime.now()

# get date time
kar_tz = pytz.timezone('Asia/Karachi')

# make it timezone aware
kar_tz = kar_tz.localize(dt)


print(kar_tz)


# now we can change time zone for that too...
dt_east = kar_tz.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)


# Get List of All Timezones
# for tz in pytz.all_timezones:
#     print(tz)


dt = datetime.datetime.now(tz=pytz.timezone('Asia/Karachi'))

print("Local Timezone aware datetime is: ", dt)
print(dt.isoformat())

print(type(dt))

# datetime to string
dt_str = dt.strftime('%B %d, %Y')

print(dt_str, " type is ", type(dt_str))

# convert string to datetime
dt_dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt_dt, " and type is: ", type(dt_dt))










