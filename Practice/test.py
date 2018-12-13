import sys
import time
import datetime
import calendar

a=[]
a=calendar.day_name
print(a)

# astim=time.asctime(time.localtime())
# # time.struct_time(())
# # time.strptime(a,"%d/%m/%y")
# # b=time.strftime("%d-%m-%Y %H %M %S %Z -0530", a)
# b=datetime.date(2017,12,3).timetuple()
# c=datetime.timedelta(days=4)

# c.total_seconds()
# print("astim "+ astim)
# print(b)
# print(c.total_seconds())
# print(datetime.date.today())
a=time.struct_time(datetime.datetime(2000,3,4).timetuple())
print(time.struct_time(datetime.datetime(2020,3,4).timetuple()))
print(time.strptime("30 November 2001", "%d %B %Y"))

# print(sys.path)