import time
import datetime

month = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May",
         6: "June", 7: "July", 8: "August", 9: "September", 10: "October",
         11: "November", 12: "December"}

date = datetime.datetime(1970, 1, 1)
now = datetime.datetime.now()
value = round(now.timestamp() - date.timestamp(), 4)
prefix = "Seconds since January 1, 1970:"
end = "in scientific notation"
print(prefix, format(value, ','), "or", "%.2e" % value, end)
print(time.strftime("%b %d %Y", time.gmtime()))


# print(month[now.month][0:3], now.day, now.year)
# date = gmtime(0)
# now = gmtime()
# str = strftime("%S", gmtime(0))
# print(date)
# print(str)
# print(now)
# print(asctime(date))
