import time as time
import datetime as dt

# d=time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0,tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)
# d=time.struct_time(tm_year=2022, tm_mon=1)
c=time.gmtime(1944865856)
m=time.struct_time((2031, 8, 19, 0, 30, 56, 1, 231,0))
d=time.strftime("%d-%m-%Y %I:%M:%S:%p.%z",c)
s=dt.datetime(2000,1,1,0,0,0).timetuple()

a=time.ctime(1944865856.6666)
# c=time.gmtime()# a=time.timezone()
b=dir(time)
print(a)
print(c)
print(d)
print(m)
print(b)
print(s)
