import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.month)
print(x.hour)
print(x.second)
print(x.day)

print(datetime.datetime(2020,2,1))

# Month
print(x.strftime("%B"))
print(x.strftime("%b"))

# Day of the week
print(x.strftime("%A"))
print(x.strftime("%a"))

# Week number of the month
print(x.strftime("%w"))

# Date
print(x.strftime("%d"))

# Month in number format
print(x.strftime("%m"))

# Year 
print(x.strftime("%y"))
print(x.strftime("%Y"))

# Hour of 24 hour clock
print(x.strftime("%H"))

# Hour of 12 hour clock
print(x.strftime("%I"))

# Minute of clock
print(x.strftime("%M"))

# Second of clock
print(x.strftime("%S"))

# AM PM
print(x.strftime("%p"))
print(x.strftime("%P"))

# microseconds
print(x.strftime("%f"))

# UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive)
print(x.strftime("%z"))

# Time zone name (empty string if the object is naive).
print(x.strftime("%Z"))

# Day no. of year
print(x.strftime("%j"))



