from datetime import datetime
from time import mktime

timer_str = "2009-11-10T23:00:00Z"
time_fmt = "%Y-%m-%dT%H:%M:%SZ"
dt = datetime.strptime(timer_str, time_fmt)
time_tuple = dt.timetuple()
epoch = mktime(time_tuple)
print(epoch)
