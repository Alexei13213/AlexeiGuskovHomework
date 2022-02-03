#import calendar

# print(calendar.month(2022, 1))

# day = calendar.month(2022, 1, w=5, l=1)
# print(day)
# print(type(day))
#
# day = calendar.calendar(2022, w=1, l=1, c=2, m=1)
# print(day)
#
# print(calendar.weekday(2022, 2, 2))
# print(calendar.isleap(2024)) # vesokosnii god
# print(calendar.leapdays(2020, 2025))

import time

# time.sleep(5)
# print("Hello world")


# Unix timestamp
# start = time.time()
#
# time.sleep(7)
#
# stop = time.time()
#
# print(stop - start)


print(time.asctime())
print(type(time.asctime()))
print(time.gmtime())
print(type(time.gmtime))
time_data = time.gmtime()
print(time_data[3] + 2)

print(time_data[0:4])