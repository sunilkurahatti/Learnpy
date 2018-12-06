import time as dt

# d=dt.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0,tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)
# d=dt.struct_time(tm_year=2022, tm_mon=1)
c=dt.gmtime(1944865856)
d=dt.strftime("%d-%m-%Y %I:%M:%S:%p.%z",c)

a=dt.ctime(1944865856.6666)
# c=dt.gmtime()# a=dt.timezone()
b=dir(dt)
print(a)
print(c)
print(d)
print(b)