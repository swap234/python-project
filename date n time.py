#date and time:
import datetime as dt
current_date=dt.date.today()
print(current_date)

import datetime as dt
datetime_obj=dt.datetime(2022,11,23,12,34,45,789)
print(datetime_obj)

import datetime as dt
time1=dt.time(11,23,43,567)
print(time1)
print(dt.datetime.now())

#datetime.timedelta class:
import datetime as dt
c_time=dt.datetime.now()
nxt_yr=dt.datetime(2023,1,1)
timeremaining=(nxt_yr-c_time)
print(timeremaining)

#strf method:
import datetime as dt
c_time=dt.datetime.now()
string_data=c_time.strftime("%A,%B,%d,%Y")
print(string_data)
